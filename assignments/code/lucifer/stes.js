const texts = document.querySelector(".texts");

window.SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

  //speech
  function readOut(message) {
    const speech = new SpeechSynthesisUtterance();
    speech.text = message;
    speech.volume = 1;
    window.speechSynthesis.speak(speech);
    console.log("Speaking out");
    // createMsg("jmsg", message);
  }
  
  function readOutLang(message,lang) {
    const speech = new SpeechSynthesisUtterance();
    speech.lang = lang
    let voices = speechSynthesis.getVoices()
    let z;
    voices.forEach((v) => {
      if(v.lang.includes(lang)){
        z = v
      }
    })
    speech.voice = z
    speech.text = message;
    speech.volume = 1;
    console.log(message);
    window.speechSynthesis.speak(speech);
    console.log("Speaking out - translated");
    // createMsg("jmsg", message);
  }

const recognition = new SpeechRecognition();
recognition.interimResults = true;

let p = document.createElement("p");

recognition.addEventListener("result", (e) => {
  texts.appendChild(p);
  const text = Array.from(e.results)
    .map((result) => result[0])
    .map((result) => result.transcript)
    .join("");

  p.innerText = text;
  if (e.results[0].isFinal) {
    if (text.includes("how are you")) {
      p = document.createElement("p");
      p.classList.add("replay");
      p.innerText = "I am fine,how u ";
      readOut(p.innerText);
      texts.appendChild(p);
    }
    
    if (
      text.includes("i am fine")||
      
      text.includes("awesome")||
      text.includes("fine")||
      text.includes("Mast") 
    ) {
      p = document.createElement("p");
      p.classList.add("replay");
      p.innerText = "nice";
      readOut(p.innerText);
      texts.appendChild(p);
    }
    if (
      text.includes("what's your name") ||
      text.includes("what is your name")
    ) {
      p = document.createElement("p");
      p.classList.add("replay");
      p.innerText = "My Name is Ishan";
      readOut(p.innerText);
      texts.appendChild(p);
    }
    if (
      text.includes("hello")
    ) {
      p = document.createElement("p");
      p.classList.add("replay");
      p.innerText = "naamaasstttee";
      readOut(p.innerText);
      texts.appendChild(p);
    }
    
    if (
      text.includes("namaste")
    ) {
      p = document.createElement("p");
      p.classList.add("replay");
      p.innerText = "ji";
      readOut(p.innerText);
      texts.appendChild(p);
    }
    if (text.includes("open my Instagram")) {
      p = document.createElement("p");
      p.classList.add("replay");
      p.innerText = "opening instagram account";
      readOut(p.innerText);
      texts.appendChild(p);
      console.log("opening instagram");
      window.open("https://www.instagram.com/ipoojabijlani/");
    }

    if (text.includes("open Google")) {
      readOut("opening google");
      window.open("https://www.google.com/");
    }
  
    if (text.includes("search for")) {
      readOut("here's your result");
      let input = text.split("");
      input.splice(0, 11);
      input.pop();
      input = input.join("").split(" ").join("+");
      window.open(`https://www.google.com/search?q=${input}`);
    }
  
    if (text.includes("open YouTube")) {
      p = document.createElement("p");
      p.classList.add("replay");
      p.innerText = "opening YouTube";
      texts.appendChild(p);
      console.log("opening YouTube");
      window.open("https://www.youtube.com/");
      readOut(p.innerText);
    }
    if (text.includes("open my YouTube")) {
      p = document.createElement("p");
      p.classList.add("replay");
      p.innerText = "opening youtube channel";
      texts.appendChild(p);
      console.log("opening youtube");
      window.open("https://www.youtube.com/channel/UC_2uXXtiLZIH00M-DYuSIbw");
      readOut(p.innerText);
    }
    p = document.createElement("p");
  }
});

recognition.addEventListener("end", () => {
  recognition.start();
});
recognition.start();
