if (window.location.pathname == '/') {
    loadPage('index');
}
else {
    loadPage(window.location.pathname.substr(1));
}


resizeSidebar = function () {
    height = $(window).height();
    $('#menu').height(height);
};
var url;
$(document).ready(function () {
    url = window.location.pathname;
    resizeSidebar();


});

$(window).resize(resizeSidebar);

function loadPage(name) {
    $('#content').load('pages/' + name, function () {
        $(this).hide().fadeIn("slow");
    });
    //window.location.pathname=name;
    window.history.pushState("", "", '/' + name);
}

loginCallback = function (response) {
    data = JSON.parse(response);
    if (data['code'] == 310) {
        location.reload();
    }
};

function login() {
    email = $('#email-input').val();
    password = $('#password-input').val();

    request = {
        email: email,
        password: password
    };
    $.ajax({
        type: 'POST',
        url: '/user/login',
        success: loginCallback,
        data: request
    });
}

logoutCallback = function (response) {
    data = JSON.parse(response);
    if(data['successful']) {
        location.reload();
    }
};

function logout() {

    $.ajax({
        type: 'POST',
        url: '/user/logout',
        success: logoutCallback,
        data: {logout: true}
    })
}