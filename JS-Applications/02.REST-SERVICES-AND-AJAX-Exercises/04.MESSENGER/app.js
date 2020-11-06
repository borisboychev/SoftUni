function attachEvents() {
  const url = "https://rest-messanger.firebaseio.com/messanger.json";
  let btnSubmit = document.getElementById("submit");
  let btnRefresh = document.getElementById("refresh");
  let messagesTextarea = document.getElementById("messages");

  btnRefresh.addEventListener("click", () => refresh(url, messagesTextarea));
  btnSubmit.addEventListener("click", () => submit(url));

  function refresh(url, textarea) {
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        let result = Object.values(data).reduce(
          (messages, message) =>
            (messages += `${message.author}: ${message.content}\n`)
        );

        textarea.textContent = result;
      });
  }

  function submit() {
    let author = document.getElementById("author");
    let content = document.getElementById("content");
    fetch(url, {
      method: "POST",
      body: JSON.stringify({ author: author.value, content: content.value }),
    });
  }
}

attachEvents();
