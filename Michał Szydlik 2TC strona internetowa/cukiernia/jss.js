function read()
{
	var y = document.getElementById("paczz").value;	
	var x = document.getElementById("kremm").value;
	if (y.length == 0 || x.length == 0)
	{
		document.getElementById("b1").innerHTML = "oba polach muszą być uzupełnione";
	}else if (isNaN(x) || isNaN(y))
	{
		document.getElementById("b1").innerHTML = "w obu polach muszą znajdować się liczby";
	}else
	{
		document.getElementById("b1").innerHTML = "";
		document.getElementById("wpacz").innerHTML = x*0.9;
		document.getElementById("wkrem").innerHTML = y*4.5;
		var suma = ((parseInt(x)*0.9)+(parseInt(y)*4.5));
		document.getElementById("suma").innerHTML = suma;
	}
}
	