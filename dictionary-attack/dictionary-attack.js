var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

function checkPassword() {
  var password = document.getElementById("pw").value;
  for (var i=0; i<wordsList.length;i++) {
    if (password == wordsList[i]) {
        document.getElementById("results").innerHTML="try a new one!";
        break;
    }
    else {
      document.getElementById("results").innerHTML="good password!";
    }
  }
}
