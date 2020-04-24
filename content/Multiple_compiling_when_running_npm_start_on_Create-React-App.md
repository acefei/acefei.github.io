Title: Multiple compiling when running npm start on Create-React-App (CRA)
Date: 2020-04-24 16:59
Category: Development
Tags: React
Authors: Ace Fei

[TOC]

## Causation
I was writing a mock API server using json-server as a backend for a react project and created a db.json file with some data. Meanwhile, I want to read the data in react, because of the create-react-app imports restriction outside of src directory, I created a soft link in src for db.json.
Then I started to test my UI running `npm start`, when I submitted some data on the component, the web browser will auto-refresh.

## Analysis
`npm start` actually excute `react-script start` and it will watch all files under src directory and will compile react src while any file changed. that is why the web browser will auto-refresh.

## Solution
Given CRA was involved webpack that was preconfigured to work in a specific way. If the project needs more customization, we have to "eject" and customize it, but then we will need to maintain this configuration.

Thanks to [react-app-rewired](https://github.com/timarney/react-app-rewired) that provide a way to tweak the create-react-app webpack config(s) without using 'eject' and without creating a fork of the react-scripts.

1. `npm install react-app-rewired --save-dev`

2. 'Flip' the existing calls to react-scripts in npm scripts for start
```
  /* package.json */
  "scripts": {
-   "start": "react-scripts start",
+   "start": "react-app-rewired start",
  }
```

3. Create a config-overrides.js file in the root directory and tweak the config according to [devServer.watchOptions](https://webpack.js.org/configuration/dev-server/#devserverwatchoptions-)
```
/* config-overrides.js */
module.exports = {
  devServer(configFunction) {
    return (proxy, allowedHost) => {
      const config = configFunction(proxy, allowedHost);
      config.watchOptions.ignored = ['**/db.json', 'node_modules'];
      return config;
    };
  },
};
```

That is it, Work like a charm.
