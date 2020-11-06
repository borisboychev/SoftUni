function loadRepos() {
  const httpReq = new XMLHttpRequest();
  const userElement = document.getElementById("username");
  const reposElement = document.getElementById("repos");

  httpReq.addEventListener("loadend", function () {
    let repos = JSON.parse(this.responseText);

    reposElement.innerHTML = repos.map(
      (x) => `<li><a href="${x.html_url}" target="_blank">${x.name}</a></li>`
    );
  });

  const url = `https://api.github.com/users/${userElement.value}/repos`;

  httpReq.open("GET", url);
  httpReq.send();
}
