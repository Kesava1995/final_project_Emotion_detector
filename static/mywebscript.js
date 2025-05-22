let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value.trim();

    // Check for empty input
    if (!textToAnalyze) {
        document.getElementById("system_response").innerHTML = "Please enter some text before analyzing.";
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                // Show error message returned from Flask
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            }
        }
    };

    // Proper URL encoding for the text
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};