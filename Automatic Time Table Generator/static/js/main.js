
function showPophod(e){
  var x = document.getElementById("hodModal");
  if(x.style.display=="none"){
	x.style.display="block";
	x.className+=' show';
  }else{
	x.style.display="none";
  }
}
function showPopfaculty(e){
  var x = document.getElementById("facultyModal");
  if(x.style.display=="none"){
	x.style.display="block";
	x.className+=' show';
  }else{
	x.style.display="none";
  }
}

function split(e){
  var x = document.getElementById("hodlogin");
  var y = document.getElementById("hodsignup");
  if(e.getAttribute("href")=="#login"){
	x.style.display="block";
	y.style.display="none";
  }else{
	y.style.display="block"
	x.style.display="none";
  }
}

function split1(e){
  var x = document.getElementById("facultylogin");
  var y = document.getElementById("facultysignup");
  if(e.getAttribute("href")=="#login"){
	x.style.display="block";
	y.style.display="none";
  }else{
	y.style.display="block"
	x.style.display="none";
  }
}
