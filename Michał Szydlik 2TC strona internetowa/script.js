var date = new Date();
var day = date.getDate();
if (day<10)
{
	day = "0"+day;
}
var month = date.getMonth();
if (month==0) month = "stycznia";
else if (month==1) month = "lutego";
else if (month==2) month = "marca";
else if (month==3) month = "kwietnia";
else if (month==4) month = "maja";
else if (month==5) month = "czarwca";
else if (month==6) month = "lipca";
else if (month==7) month = "sierpnia";
else if (month==8) month = "września";
else if (month==9) month = "października";
else if (month==10) month = "listopada";
else if (month==11) month = "grudnia";	
var year = date.getFullYear();
var today = "Data: "+day+" "+month+" "+year;
function Myfunction()
{
	document.getElementById("info").innerHTML = '<font size="6">JavaScript jest to skryptowy język programowania, stworzony przez firmę Netscape, najczęściej stosowany na stronach internetowych.<br> Służy najczęściej do zapewnienia interakcji poprzez reagowanie na zdarzenia, walidacji danych wprowadzanych w formularzach lub tworzenia złożonych efektów wizualnych. Skrypty JavaScriptu uruchamiane przez strony internetowe mają znacznie ograniczony dostęp do komputera użytkownika.<br> link do strony o sposobach osadzania skryptów:<a href="http://www.kurshtml.edu.pl/js/osadzenie_skryptu,index.html" strony>link</a> </font>';
}
function Myfunction1()
{
	document.getElementById("info").innerHTML = '<font size="6">Może zostać użyty np. do wczytywania aktualnej daty <br>var day = date.getDate();<br><br>wypisaniu tekstu na ekranie <br>document.write("Hello Word")<br><br>lub obsługi plików cookie<br>document.cookie = "Nazwa1=wartosc1; expires=Mon, 18 May 2009 23:00:10 GMT; domain=script.pl";</font>';
}
function Myfunction2()
{
	document.getElementById("info").innerHTML = '<font size="6">adres e-mail: schoolmich2000@gmail.com<br>Telefon kontaktowy: 693881197<br>adres: Plac Zamkowy 4, Warszawa <br> Kod pocztowy: 00-277</font>';
}