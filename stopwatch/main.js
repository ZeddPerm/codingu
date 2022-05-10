var timer = document.getElementById("timer");
var timerdiv = document.getElementById("timerdiv")
var countdown = document.getElementById("countdown")
var start = document.getElementById("start")
var stopbutton = document.getElementById("stop")
console.log(timer)
var scount = 00
var mcount = 00
var hcount = 00
var countdowncount = 0
var scountdowncount = 9
var mcountdowncount = 9
var hcountdowncount = 9
function timerprocess() {
    console.log('in loop');
    timer.innerHTML = `${hcount}:${mcount}:${scount}`;
    console.log(timer);
    if (scount >= 59) {
        scount = 0
        mcount++
    }
    if (mcount >= 59) {
        mcount = 0
        hcount++
    }
    else {
        scount++
    }
}
function startcountdown() {
    console.log('in loop');
    console.log(countdowncount);
    timerdiv.innerHTML = `<h1 id="timer">${hcountdowncount}:${mcountdowncount}:${scountdowncount}</h1>`;
    timer = document.getElementById("timer");
    console.log(countdowncount);
    console.log(timer);
    if (hcountdowncount == 0 && mcountdowncount == 0 && scountdowncount == 0) {
        timerdiv.innerHTML = `<h1 id="timer">Countdown complete.</h1>`;
        clearInterval(countdowntimerstart);
    }
    if (mcountdowncount <= 0 && hcountdowncount != 0) {
        mcountdowncount = 60;
        hcountdowncount--;
    }
    if (scountdowncount <= 0) {
        scountdowncount = 59;
        mcountdowncount--;
    }
    else {
        scountdowncount--
    }
    console.log(countdowncount);
}
function begincountdowntimer() {
    countdowncount = timer.value;
    console.log(timer.innerHTML);
    console.log('a',countdowncount);
    var hms = String(countdowncount).split(/\r?\n/);
    scountdowncount = parseInt(hms[2]);
    mcountdowncount = parseInt(hms[1]);
    hcountdowncount = parseInt(hms[0]);
    countdowntimerstart = setInterval(startcountdown, 100);
}
function starttimer() {
    stopbutton.innerHTML = `<button id="stop" style="display:inline" onclick="stoptimer()">Stop</button>`;
    console.log('button clicked');
    timerstart = setInterval(timerprocess, 100);
    start.innerHTML = `<button id="start" style="display:none" onclick="starttimer()">Start</button>`;
}
function stoptimer() {
    start.innerHTML = `<button id="start" style="display:inline" onclick="starttimer()">Start</button>`;
    console.log('cleared');
    clearInterval(timerstart);
    stopbutton.innerHTML = `<button id="stop" style="display:none" onclick="stoptimer()">Stop</button>`;
}
function resettimer() {
    timer.innerHTML = '0';
    count = 0;
}
function countdowntimer() {
    timer.outerHTML = `<textarea id="timer" placeholder="Please input your time in this format: hours:minutes:seconds"></textarea>`;
    timer = document.getElementById("timer");
    countdown.outerHTML = `<button id="countdown" onclick="begincountdowntimer()">Countdown</button>`;
    console.log(timer);
}
