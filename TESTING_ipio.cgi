<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="de-de">
<head>
  
  
  <title>ELV IP-IO-Interface IPIO 88</title>
  <meta http-equiv="expires" content="0; URL=/ipio.cgi">
  
  <meta http-equiv="refresh" content="15; URL=/ipio.cgi">
  
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body style="color: #FF6000; background-color: #000015; direction: ltr;" 
alink="#FF6000" link="#FF6000" vlink="#FF6000">
<table align="center" border="0" width="600">
  <tbody>
    <tr height="70">
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td align="center" valign="middle" width="170">&nbsp;<img src="elv.gif">&nbsp;</td>
      <td align="center" valign="middle" width="300">
      
      <h1>IP-IO-Interface
IPIO88</h1>
      </td>
      <td align="center" valign="middle" width="170">&nbsp;<font size="1">V1.4</font>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr height="80">
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  
  </tbody>
</table>
<form name="Main" action="ipio.cgi" method="get">
<input value="main" name="pg" type="hidden">
  
  <table align="center" border="0" width="500">
    <tbody>
      <tr align="center" height="15" valign="bottom">
        <td width="20%">&nbsp;&nbsp;</td>
        <td width="10%">&nbsp;1&nbsp;</td>
        <td width="10%">&nbsp;2&nbsp;</td>
        <td width="10%">&nbsp;3&nbsp;</td>
        <td width="10%">&nbsp;4&nbsp;</td>
        <td width="10%">&nbsp;5&nbsp;</td>
        <td width="10%">&nbsp;6&nbsp;</td>
        <td width="10%">&nbsp;7&nbsp;</td>
        <td width="10%">&nbsp;8&nbsp;</td>
      </tr>
      <tr align="center" height="35" valign="middle">
        <td width="20%">&nbsp;Eingänge:&nbsp;</td>
        <td width="10%">&nbsp;
<input name="in1" checked="checked" size="1" disabled="disabled" type="checkbox">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="in2"  size="1" disabled="disabled" type="checkbox">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="in3"  size="1" disabled="disabled" type="checkbox">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="in4"  size="1" disabled="disabled" type="checkbox">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="in5"  size="1" disabled="disabled" type="checkbox">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="in6"  size="1" disabled="disabled" type="checkbox">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="in7"  size="1" disabled="disabled" type="checkbox">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="in8"  size="1" disabled="disabled" type="checkbox">&nbsp;</td>
      </tr>
      <tr align="center" height="35" valign="middle">
        <td width="20%">&nbsp;Ausgänge:&nbsp;</td>
        <td width="10%">&nbsp;
<input name="out1" checked="checked" type="checkbox" onclick="submit()">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="out2" checked="checked" type="checkbox" onclick="submit()">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="out3" checked="checked" type="checkbox" onclick="submit()">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="out4" checked="checked" type="checkbox" onclick="submit()">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="out5" checked="checked" type="checkbox" onclick="submit()">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="out6" checked="checked" type="checkbox" onclick="submit()">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="out7" checked="checked" type="checkbox" onclick="submit()">&nbsp;</td>
        <td width="10%">&nbsp;
<input name="out8" checked="checked" type="checkbox" onclick="submit()">&nbsp;</td>
      </tr>
    
    </tbody>

  <table align="center" border="0" width="700">
    <tbody>
      <tr align="center" height="15" valign="middle">
        <td width="25%">&nbsp;&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;</td>
      </tr> 
      <tr align="center" height="15" valign="bottom">
        <td width="25%">&nbsp;&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;<input value="Alle Ausgänge an" name="all_on" type="submit">&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;<input value="Alle Ausgänge aus" name="all_off" type="submit">&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;</td>
      </tr>

      <tr align="center" height="50" valign="middle">
        <td width="25%">&nbsp;&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;</td>
        <td width="25%">&nbsp;&nbsp;</td>
      </tr> 
    </tbody>  
  </table>

<input value="main" name="end" type="hidden">
</form>
<table align="center" border="1" width="700">
  <tbody>
    <tr align="center" valign="middle">
      <td width="33%"><a href="/password.cgi">Benutzer/Passwort</a></td>
      <td width="34%"><a href="/network.cgi">Systemeinstellungen</a></td>
      <td width="33%"><a href="ioports.cgi">Ein- und Ausgänge</a></td>
    </tr>
  
  </tbody>
</table>
<table align="center" border="0" width="700">
  <tbody>
    <tr height="50">
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr align="center" valign="middle">
      <td width="33%">© 2009 ELV Elektronik AG</td>
      <td width="34%"></td>
      <td width="33%"></td>
    </tr>
  
  </tbody>
</table>
.
</body>
</html>
