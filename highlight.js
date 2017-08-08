/*global URL, fetch, Prism */
var url = new URL(document.location);
var params = url.searchParams;
var code_url = params.get('url');
if (code_url) {
  fetch(code_url)
    .then((res) => res.text())
    .then((txt) => {
      var code = document.getElementById('code');
      code.innerText = txt;
      //FIXME
      code.classList.add('.language-cpp');
      Prism.hooks.add('before-highlight', function (env) {
        env.code = env.element.innerText;
      });
      Prism.highlightElement(code);
    });
}
