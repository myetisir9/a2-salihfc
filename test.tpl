
<h1> Comment Section </h1>

% for comment in comments:
	
	<p> from {{ comment['author'] }} : {{ comment['content'] }} </p>
	
% end



<form action="/comments" method="post">
  User Name:<br>
  <input type="text" name="author" value="">
  <br>
  
  Password:<br>
  <input type="password" name="password" value="">
  <br>
  
  Comment:<br>
  <input type="text" name="content" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 

% if { wrongpw } ==  True:
	<p> Wrong Password </p>
% end
