/**
 * Created by jamy on 12/24/14.
 */
// here 1 percent left equal to nine pixel

	function FetchScore() {
		var dummyData = [{name: 'jamy', score: 20, time: "1 jan 2016"},{name: 'sadun', score: 10, time: "1 jan 2016"},{name: 'dipu', score: 50, time: "1 jan 2016"}]
		var dummyHtml = "<table>";
		fetch('http://dummy.restapiexample.com/api/v1/employees',{ mode: 'no-cors' }) // Call the fetch function passing the url of the API as a parameter
		.then(function(d) {
			for(var i=0;i<dummyData.length; i++)
			{
				dummyHtml += "<tr><td><b>Name: </b>"+dummyData[i].name+ "</td><td><b>Score: </b>"+dummyData[i].score+ "</td><td><b>Time: </b>" +dummyData[i].time +"</td></tr>"
			}
			dummyHtml += "</table>";
			document.getElementById("scoreContent").innerHTML = dummyHtml;
		})
		.catch(function() {
			// This is where you run code if the server returns any errors
		});
	}
	

	
	async function postData(url = '', data = {}) {
	  // Default options are marked with *
	  const response = await fetch(url, {
		method: 'POST', // *GET, POST, PUT, DELETE, etc.
		mode: 'cors', // no-cors, *cors, same-origin
		cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
		credentials: 'same-origin', // include, *same-origin, omit
		headers: {
		  'Content-Type': 'application/json'
		  // 'Content-Type': 'application/x-www-form-urlencoded',
		},
		redirect: 'follow', // manual, *follow, error
		referrer: 'no-referrer', // no-referrer, *client
		body: JSON.stringify(data) // body data type must match "Content-Type" header
	  },{ mode: 'no-cors' });
	  return await response.json(); // parses JSON response into native JavaScript objects
	}
	
	async function SaveScore()
	{
		var demodata = {Name: window.Name, Score: 1}
		try {
		  const data = await postData('http://dummy.restapiexample.com/api/v1/create', demodata);
		  console.log(JSON.stringify(data)); // JSON-string from `response.json()` call
		} catch (error) {
		  console.error(error);
		}
	}

	function ShowHighScoreModal()
	{
		if(window.HasGameStart != 1)
		{
			$("#myModal").toggle();
			$("#background").toggle();
			FetchScore();
		}
	}
	
	function GetName() {
	  var person = prompt("Please enter your name", "Harry Potter");
	  if (person == null || person == "") {
		GetName();
	  }
	  else window.Name = person;
	}

$(document).ready(function () {
    //alert('hellow')
    //$("#background div#bird").css({'background-image': 'url(resource/bird.png)'});
	GetName();
    document.getElementById("welcomeMessage").innerHTML="Click here to Start " + window.Name;
    var x=-1;
    var Score= 0;
    var scoreR=[];
    var myinterval=null,speedInterval=null;

    var moveObjectvar=false;

    var marginTop=25;
    var percent="%";

    var gspeed= 0.1,gacc=0.005;

    var speed= 0.4,acc=0.001;

    var birdtimer= 150, birdtimermod=1;

    var cloudmarginleft1=Math.floor((Math.random() * 10) + 80);
    var cloudmarginleft2=Math.floor((Math.random() * 10) + 120);
    var cloudmarginleft3=Math.floor((Math.random() * 10) + 160);

    var cloudSpeed=0.1;

    var moveCloudVar=true;

    $("#cloud1").css("margin-top",Math.floor((Math.random() * 35) + 1)+"%");

    $("#cloud2").css("margin-top",Math.floor((Math.random() * 35) + 1)+"%");

    $("#cloud3").css("margin-top",Math.floor((Math.random() * 35) + 1)+"%");

    $("#cloud1").css("margin-left",cloudmarginleft1+"%");

    $("#cloud2").css("margin-left",cloudmarginleft2+"%");

    $("#cloud3").css("margin-left",cloudmarginleft3+"%");

    window.reload= function (){window.location.reload();}




    function detectCollision(){
        var birdPosition = $('#bird').offset();
        var birdWidth=$('#bird').width();
        var cloudWidth=$('#cloud1').width();

        var birdHeight=$('#bird').height();
        var cloudHeight=$('#cloud1').height();
        for(i=1;i<4;i++){
            var cloudPosition = $('#cloud'+i).offset();
            if(cloudPosition.left<=birdPosition.left+birdWidth-20){
                //alert('bal');
                //console.log(cloudPosition.left);
                //console.log(birdPosition.left+birdWidth);
                if(cloudPosition.left+cloudWidth>=birdPosition.left+20){
                    if(cloudPosition.top+cloudHeight>=birdPosition.top+20&&cloudPosition.top<=birdPosition.top+birdHeight-50){
                        document.getElementById('audiotag1').pause();
                        document.getElementById('audiotag2').play();
                        return true;
                    }
                    scoreR[i]=true;
                }
                else if(scoreR[i]==true){
                    if(cloudPosition.left+cloudWidth<birdPosition.left){
                        Score+=1;
                        document.getElementById("Score").innerHTML=Score;
                        scoreR[i]=false;
                    }
                }
            }
        }
        return false;
    }
    function animateBackground(){
        var s= x+"px 0";
        $("#background").css("background-position",s);
        x-=1;
        if(moveObjectvar){
            marginTop-=speed;
            var s= marginTop+percent;
            speed -=acc;

            $("#bird").css("marin-top",s);
            if(birdtimermod%birdtimer==0) {
                resetvalue();
                birdtimermod=1;
                moveObjectvar = false;
            }
            else{
                birdtimermod+=1;
                //console.log(birdtimermod);
            }
        }

        if(moveCloudVar) {
            moveCloud();
            if(detectCollision()){
                $("#background div#bird").css("background-image","url('resource/bird4.gif')");
                moveCloudVar=false;
                moveObjectvar=false;
            }
        }
        gravity();

        //console.log(s);
    }
    function increaseCloudSpeed(){
        //cloudSpeed += 0.01;
    }
    function moveCloud(){
        var s1= cloudmarginleft1+percent;
        var s2= cloudmarginleft2+percent;
        var s3= cloudmarginleft3+percent;
        $("#cloud1").css("margin-left",s1);
        $("#cloud2").css("margin-left",s2);
        $("#cloud3").css("margin-left",s3);

        cloudmarginleft1-=cloudSpeed;
        cloudmarginleft2-=cloudSpeed;
        cloudmarginleft3-=cloudSpeed;
        if(cloudmarginleft1<-20){
            cloudmarginleft1=Math.floor((Math.random() * 10) + 100);
            $("#cloud1").css("margin-top",Math.floor((Math.random() * 35) + 1)+"%");
            $("#cloud1").css("margin-left",cloudmarginleft1+"%");
            increaseCloudSpeed();
        }
        else if(cloudmarginleft2<-20){
            cloudmarginleft2=Math.floor((Math.random() * 10) + 100);
            $("#cloud2").css("margin-top",Math.floor((Math.random() * 35) + 1)+"%");
            $("#cloud2").css("margin-left",cloudmarginleft2+"%");
            increaseCloudSpeed();
        }
        else if(cloudmarginleft3<-20){
            cloudmarginleft3=Math.floor((Math.random() * 10) + 100);
            $("#cloud3").css("margin-top",Math.floor((Math.random() * 35) + 1)+"%");
            $("#cloud3").css("margin-left",cloudmarginleft3+"%");
            increaseCloudSpeed();
        }
    }

    function resetgvalue(){
        gspeed=0.1;gacc=0.005;
    }
    function resetvalue(){
        speed=0.4;acc=0.001;
    }
    function resetCloud(){
         cloudmarginleft1=Math.floor((Math.random() * 10) + 80);
         cloudmarginleft2=Math.floor((Math.random() * 10) + 120);
         cloudmarginleft3=Math.floor((Math.random() * 10) + 160);
    }

    function moveObject(param){
        if(param=="bottom"){
            var s= marginTop+percent;
            $("#bird").css("margin-top",s);
            marginTop+=3;
        }
        else if(param=="top"){
            var s= marginTop+percent;
            $("#bird").css("margin-top",s);
            marginTop-=8;
        }
        resetgvalue();
    }

    function gravity(){
        var s= marginTop+percent;
        if(marginTop<43&&marginTop>=-3) {
            $("#bird").css("margin-top", s);
            marginTop += gspeed;
            gspeed += gacc;
            //console.log(marginTop)
        }
        else if(marginTop<-3){
            document.getElementById('audiotag2').play();
            $("#background div#bird").css("background-image","url('resource/bird4.gif')");
            moveCloudVar=false;
            moveObjectvar=false;
            marginTop=-3;
        }
        else{
            //marginTop=25;
			window.HasGameStart = 0;
            document.getElementById('audiotag1').pause();
            document.getElementById("welcomeMessage").innerHTML="Game Over "+window.Name+"<br> Your Score is:"+Score+" <a onclick='reload();return false;'>play again?</a>";
            $("#background div#bird").css("background-image","url('resource/bird4.gif')");
            resetgvalue();
            resetvalue();
            clearInterval(myinterval);
            clearInterval(speedInterval);
            myinterval=null;
            cloudSpeed=0.1;
            moveObjectvar=false;
			SaveScore();
        }
    }

/*
    $("#start").click(function() {
        //alert(document.getElementById("start").innerHTML);
        if(document.getElementById("start").innerHTML =="Pause"){
            document.getElementById("start").innerHTML = "Start";
        }
        else{
            document.getElementById("start").innerHTML = "Pause";
        }
        if(!myinterval) {
            myinterval=setInterval(animateBackground, 10);
            //setInterval(myinterval);
        }
        else if(myinterval){
            clearInterval(myinterval);
            myinterval=null;
        }
    });
*/

    $("#background").click(function() {
		//FetchScore();
		window.HasGameStart = 1;
        document.getElementById("welcomeMessage").innerHTML="";
        if(!myinterval) {
            //resetCloud();
            //document.getElementById("start").innerHTML = "Start";
            myinterval = setInterval(animateBackground, 10);
            speedInterval= setInterval(function(){cloudSpeed += 0.01;},2000)
        }
        else if(moveCloudVar){
            //document.getElementById("start").innerHTML = "Pause";
            document.getElementById('audiotag1').play();
            birdtimermod=1;
            resetgvalue();
            resetvalue();
            moveObjectvar=true;
        }
    });

    $('body').keypress(function(event) {
        if(myinterval){
            var keyCode;
            if(event.keyCode > 0)
            {
                keyCode = event.keyCode;
            }
            else if(typeof(event.charCode) != "undefined")
            {
                keyCode = event.charCode;
            }

            if(keyCode==32&&moveCloudVar){
                //moveObject('space');
                document.getElementById('audiotag1').play();
                birdtimermod=1;
                resetgvalue();
                resetvalue();
                moveObjectvar=true;
            }
        }
        //$(this).unbind('keypress');
    });





});