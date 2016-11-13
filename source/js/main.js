var test = require('./test.js');
var Devices = require('./devices.js');
var callOnLoad = require('./callList.js');

if (window.location.pathname == '/') {
  loadPage('index');

}
else {
  loadPage(window.location.pathname.substr(1));
}

var resizeSidebar = function () {
  let height = $(window).height();
  $('#menu').height(height);
};
var url;
$(document).ready(function () {
  let url = window.location.pathname;
  resizeSidebar();


});

$(window).resize(resizeSidebar);

function loadPage(name) {
  $('#content').load('/pages/' + name, function () {
    $(this).hide().fadeIn("slow");
    // console.log(name);
    // console.log(callOnLoad.default[name]);
    // console.log(!callOnLoad.default[name]);
    if(callOnLoad.default[name]) {
      // console.log('call on load');
      callOnLoad.default[name]();
    }
  });
  //window.location.pathname=name;
  window.history.pushState("", "", '/' + name);
  return false;
}

window.loadPage = loadPage;

var loginCallback = function (response) {
  let data = JSON.parse(response);
  if (data['code'] == 310) {
    document.cookie = 'session=' + data['session'];
    console.log(document.cookie);
    location.reload();
  }
};

function login() {
  let email = $('#email-input').val();
  let password = $('#password-input').val();

  let request = {
    email: email,
    password: password
  };
  $.ajax({
    type: 'POST',
    url: '/api/user/login',
    success: loginCallback,
    data: request
  });
  return false;
}
window.login = login;

var logoutCallback = function (response) {
  let data = JSON.parse(response);
  if (data['successful']) {
    location.reload();
  }
};

function logout() {

  $.ajax({
    type: 'POST',
    url: '/api/user/logout',
    success: logoutCallback,
    data: {logout: true}
  });
  return false;

}

window.logout = logout;