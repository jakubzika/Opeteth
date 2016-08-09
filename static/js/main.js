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
    return false;
}

loginCallback = function (response) {
    data = JSON.parse(response);
    if (data['code'] == 310) {
        document.cookie = 'session='+data['session'];
        console.log(document.cookie);
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
        url: '/api/user/login',
        success: loginCallback,
        data: request
    });
    return false;
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
        url: '/api/user/logout',
        success: logoutCallback,
        data: {logout: true}
    });
        return false;

}