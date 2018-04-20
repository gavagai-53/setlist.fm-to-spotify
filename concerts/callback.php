<html>
<head>
  <script type="text/javascript">
  var $code = <?php echo "'".$_GET['code']."'"; ?>;

  try {
    window.opener.onSpotifyAuth($code);
    window.close();
  } catch (err) {}
  </script>
</head>
</html>
