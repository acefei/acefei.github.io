Title: perl & cgi practice
Date: 2018-02-23 17:06
Category: Development
Tags: perl,cgi,javascript
Authors: Ace Fei


[TOC]

This article is inspired from [an practical assignment ](http://cgi.csc.liv.ac.uk/~ullrich/COMP284/assignment1N-2017-18.html), as well as I have prior knowledge of perl script, so just for fun to write this.

# Install and configure software
```
sudo yum install -y httpd perl perl-CGI
```

# Modify httpd.conf

## Load cgi module

1. `find /etc/httpd/modules/ -iname "*cgi*"`

Then we can figure out below:
`/etc/httpd/modules/mod_cgi.so`

2. Let's add that to the /etc/httpd/conf/httpd.conf file:  
`LoadModule cgi_module modules/mod_cgi.so`

## Change the directory settings in httpd.conf
Modify as below in /etc/httpd/conf/httpd.conf:
```
<Directory "/var/www/cgi-bin">
    Options +ExecCGI
    AddHandler cgi-script .cgi .pl
</Directory>
```

# Create cgi script and Test it
Create cgi script /var/www/cgi-bin/simple.pl:
```
#!/usr/bin/perl

use CGI qw/:standard/;
print
   header,
   start_html('Simple Script'),
   h1('Simple Script'),
   start_form,
   "What's your name? ",textfield('name'),p,
   "What's the combination?",
   checkbox_group(-name=>'words',
          -values=>['eenie','meenie','minie','moe'],
          -defaults=>['eenie','moe']),p,
   "What's your favorite color?",
   popup_menu(-name=>'color',
      -values=>['red','green','blue','chartreuse']),p,
   submit,
   end_form,
   hr,"\n";
if (param) {
   print
   "Your name is ",em(param('name')),p,
   "The keywords are: ",em(join(", ",param('words'))),p,
   "Your favorite color is ",em(param('color')),".\n";
}
print end_html;
```

And then you need to tell http server that these CGI scripts are allowed to be executed as programs.
chmod 755 *.cgi *.pl

Or you can target individual CGI scripts.
chmod 755 simple.pl

Invoking script in /var/www/cgi-bin to guarantee the output is fine.
```
$ ./simple.pl 
Content-Type: text/html; charset=ISO-8859-1

<!DOCTYPE html
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
         "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
<head>
<title>Simple Script</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
</head>
<body>
<h1>Simple Script</h1><form method="post" action="http://localhost" enctype="multipart/form-data">What's your name? <input type="text" name="name"  /><p />What's the combination?<label><input type="checkbox" name="words" value="eenie" checked="checked" />eenie</label><label><input type="checkbox" name="words" value="meenie" />meenie</label><label><input type="checkbox" name="words" value="minie" />minie</label><label><input type="checkbox" name="words" value="moe" checked="checked" />moe</label><p />What's your favorite color?<select name="color" >
<option value="red">red</option>
<option value="green">green</option>
<option value="blue">blue</option>
<option value="chartreuse">chartreuse</option>
</select><p /><input type="submit" name=".submit" /><div><input type="hidden" name=".cgifields" value="words"  /></div></form><hr />

</body>
</html>
```
Now restart httpd like so:
```
sudo systemctl restart httpd.service
```

Finally, open the broswer with the url:
`http://localhost/cgi-bin/simple.pl`

# Further Practice: Use javascript in Perl CGI
```
#!/usr/bin/perl

use CGI qw/:standard/;

sub login_page {
   header,
   start_html('Perl & CGI & JS'),
   h3('Login'),
   start_form,
   "Username: ", textfield('usr'), p,
   "Password:",  textfield('pwd'), p,
   submit,
   end_form,
   hr,"\n";
}

sub is_textfield_empty {
    return (param('usr') eq '' or param('pwd') eq '');
}

sub alert_and_redirect {
    my $err_msg = shift;
    my $rdurl = shift;
    my $js = <<JS;
        alert("$err_msg");
        window.location="$rdurl";
JS
    print qq(<script type="text/javascript">$js</script>);
}

sub printenv {
    foreach $var (sort(keys(%ENV))) {
        $val = $ENV{$var};
        $val =~ s|\n|\\n|g;
        $val =~ s|"|\\"|g;
        print p,"${var}=\"${val}\"";
    }
}

print login_page;

# When click submit button, it will send http POST method, otherwire send GET
if ($ENV{'REQUEST_METHOD'} eq 'POST') {
    if (is_textfield_empty) {
        alert_and_redirect "Please enter username and password!", url;
    } else {
        print printenv;
    }
}

print end_html;

```


