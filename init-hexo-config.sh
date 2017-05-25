#!/bin/sh
set -eu

theme="butterfly"
blog_name='OnePiece'

npm_install() {
    npm install hexo-theme-${theme} \
                hexo-renderer-pug \
                --save
}

hexo_config() {
    local config="_config.${theme}.yml"

    # clean default theme
    rm -rf themes/* _config.*.yml

    # use new theme
    [ -f "${config}" ] || cp node_modules/hexo-theme-${theme}/_config.yml ${config}
    perl -i -pe "s/(?<=^theme: ).*/${theme}/g"  _config.yml

    local blog_url=$(git remote -v | tail -1 | perl -pe 's#[^/]+/(.+).git.+#$1#')
    perl -i -pe "s#(?<=^url: ).*#https://${blog_url}#g"  _config.yml

    chmod 777 -R .
    echo "\n---> It is now to further configure ${config} on demand."
}

# https://hexo.io/docs/github-pages.html
action_config() {
    cp subtitle_rotation.sh ${blog_name}
    local action_file=".github/workflows/pages.yml"
    mkdir -p $(dirname ${action_file})
    [ -f "${action_file}" ] || cat > ${action_file} <<EOF
name: Pages

on:
  push:
    branches:
      - hexo # the branch where the hexo was installed

jobs:
  pages:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ${blog_name}
    steps:
      - uses: actions/checkout@v3
        with:
          token: \${{ secrets.GITHUB_TOKEN }}
          # If your repository depends on submodule, please see: https://github.com/actions/checkout
          submodules: recursive
      - name: Use Node.js 16.x
        uses: actions/setup-node@v2
        with:
          node-version: '16'
      - name: Cache NPM dependencies
        uses: actions/cache@v2
        with:
          path: node_modules
          key: \${{ runner.OS }}-npm-cache
          restore-keys: |
            \${{ runner.OS }}-npm-cache
      - name: Install Dependencies & Build
        run: npm install && npm run build
      - name: Set Subtitle
        run: bash subtitle_rotation.sh
      # https://github.com/marketplace/actions/github-pages-action#%EF%B8%8F-set-runners-access-token-github_token
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: \${{ secrets.GITHUB_TOKEN }}
          publish_dir: ${blog_name}/public
EOF
}

set_gitignore() {
    [ -f .gitignore ] || cat > .gitignore <<EOF
.DS_Store
Thumbs.db
db.json
*.log
node_modules/
public/
.deploy*/
_multiconfig.yml
EOF
}

main() {
    set_gitignore
    action_config
    [ -d "${blog_name}" ] || hexo init ${blog_name}
    cd ${blog_name}
    npm_install
    hexo_config
}

main
