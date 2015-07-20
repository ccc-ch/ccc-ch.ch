var singleargument = ["date", "logout", "shutdown", "inventory", "whoami", "pwd", "tar", "cat"];
var filesystem = ["...", "/ccc-ch", "/protokoll", "/statuten", "/faq", "/presse", "/impressum", "readme.txt"];
var bashlog = [];
var bashindex = 0;
var bodycount = 0;
var elevated = 0;
runelevated = 0;
var passwordtryouts = 0;

$(document).click(function() {
    caretdiv();
});

$(document).keydown(function(e) {
    if ( e.altKey && ( String.fromCharCode(e.which) === 't' || String.fromCharCode(e.which) === 'T' ) ) {
        e.preventDefault();
        if ( $("#content").is(":visible") ) {
            $("#content").hide();
            $("#console").show();
            caretdiv();
        } else{
            $("#content").show();
            $("#console").hide();
        }
    }
    if ( $('#console').is(':visible') ) {
     switch(e.which) {
        case 38: // up
        e.preventDefault();
        bashindex = bashindex+1;
        if(bashlog.length >= bashindex){
            $("#console_input").html(bashlog[bashlog.length-bashindex]);
            caretdiv();
        } else{
            bashindex = bashlog.length;
        }
        break;
        case 40: // down
        e.preventDefault();
        bashindex = bashindex-1;
        if(bashindex <= 0){
            bashindex = 0;
            $("#console_input").html('');
        } else{
            $("#console_input").html(bashlog[bashlog.length-bashindex]);
            caretdiv();
        }
        break;
    }
}
});

$(document).keypress(function(e) {
    if(e.which == 13) {
        e.preventDefault();
        if($('#console_input').length){
            sanitizeinput();
            input = inputarray[0];
            bashindex = 0;
            $( "<p>[<span class='console_context_2'>guest@ccc-ch.ch</span>]:"+inputraw+"</p>" ).appendTo( ".console_output" );
            if ( $( ".remove" ).length ) {
                $( ".remove" ).remove();
            }
            if(!inputraw.trim()){
            }
            else{
                $(".prompt").hide();
                bashlog.push(inputraw);
                $.ajax({
                    url: "js/bash.js",
                    dataType: "script",
                    async: false,
                    success: function() {
                    executeinput();
                    }
                });
                $(".prompt").show();
            }
        }
        else if($('#console_pw').length){
            $.ajax({
                url: "js/bash.js",
                dataType: "script",
                async: false,
                success: function() {
                passwordinput();
                }
            });
        }
        if($('#console_input').length){
            $('#console_input').html('');
        }
        else if($('#console_pw').length){
            $('#console_pw').html('');
        }
        $("html, body").animate({scrollTop:$(document).height()});
    }
});

function sanitizeinput() {
    inputraw = $('#console_input').html();
    inputraw = $.trim(inputraw);
    inputraw = inputraw.replace(/ +(?= )/g,'');
    inputarray = inputraw.split(' ');
    input = inputarray[0];
}

function placecaret(e) {
    e.focus();
    if (typeof window.getSelection != "undefined" && typeof document.createRange != "undefined") {
        var range = document.createRange();
        range.selectNodeContents(e);
        range.collapse(false);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
    } else if (typeof document.body.createTextRange != "undefined") {
        var textRange = document.body.createTextRange();
        textRange.moveToElementText(e);
        textRange.collapse(false);
        textRange.select();
    }
}

function caretdiv() {
    if( $("#console").is(":visible") ){
        if($('#console_input').length){
            focus = "#console_input";
        }
        else if($('#console_pw').length){
            focus = "#console_pw";
        }
        placecaret($(focus).get(0));
    }
}