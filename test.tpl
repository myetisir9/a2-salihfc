
<h1> hello {{name}} </h1>

% for comment in comments:
	
	<p> from {{ comment['author'] }} : {{ comment['content'] }} </p>
	
% end



<form action="/comments" method="post">
  Your Name:<br>
  <input type="text" name="author" value="">
  <br>
  Comment:<br>
  <input type="text" name="content" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 
