function passwordinput(){
    pw = $('#console_pw').html();
    if(pw == "swordfish"){
        elevated = 1;
        runelevated = 1;
        passwordtryouts = 0;
        $('.console_context').html('guest@ccc-ch.ch');
        $('#console_pw').attr('id','console_input');
        executeinput();
        caretdiv();
    }
    else if(pw !== "password" && passwordtryouts == 2){
        passwordtryouts = 0;
        $( "<p>Wrong password again. Better luck next time</p>" ).appendTo( ".console_output" );
        $('.console_context').html('guest@ccc-ch.ch');
        $('#console_pw').attr('id','console_input');
        caretdiv();
    }
    else{
        $( "<p>Wrong password try again</p>" ).appendTo( ".console_output" );
        passwordtryouts = passwordtryouts+1;
    }
}

function executeinput(){
    if($.inArray(input, singleargument)!==-1 && inputarray.length > 1){
        $( "<p>the command '"+input+"' does not accepts any parameters</p>" ).appendTo( ".console_output" );
    }
    else if($.inArray("help", inputarray ) !== -1 || $.inArray("--help", inputarray ) !== -1 || $.inArray("man", inputarray ) !== -1){
        $( "<p>That would be cheating!</p>" ).appendTo( ".console_output" );
    }
    else{
        switch (input) {
            case "sudo":
                if(inputarray.length > 1  && input == "sudo"){
                    inputarray.splice($.inArray(input, inputarray),1);
                    input = inputarray[0];
                    if(elevated == 0){
                        $("<p>We trust you have received the usual lecture from Tyler. It usually boils down to these eight things:<br /><br />#1) You do not talk about the fight club.<br />#2) You do not talk about the fight club.<br />#3) If someone says stop or goes limp, taps out, the fight is over.Only two guys to a fight.<br />#4) Only two guyst to a fight.<br />#5) One fight at a time.<br />#6) No shirts, no shoes.<br />#7) Fights will go on as long as they have to.<br />#8) If this is your first night at fight club, you have to fight.<br /><br /></p>" ).appendTo( ".console_output" );
                        $('.console_context').html('password');
                        $('#console_input').attr('id','console_pw');
                    }
                    else{
                        runelevated = 1;
                        executeinput();
                    }
                }
                else{
                    $( "<p>What should su do?</p>" ).appendTo( ".console_output" );
                }
            break;

            case "date":
            date = new Date($.now());
            $( "<p>"+date+"</p>" ).appendTo( ".console_output" );
            break;

            case "override":
            $( "<p>This isn't the movie Hackers kiddo</p>" ).appendTo( ".console_output" );
            break;

            case "logout":
            $( "<p>I'm sorry dave i'm afraid i can't do that</p>" ).appendTo( ".console_output" );
            break;

            case "shutdown":
            $( "<div class='remove'><iframe src='https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1' frameborder='0' allowfullscreen></iframe></div>" ).appendTo( ".console_output" );
            break;

            case "cat":
            $( "<div class='remove'><p><img src='js/img/nyan.png' alt='nyan'></p></div>" ).appendTo( ".console_output" );
            break;
            
            case "whoami":
            $.ajax({
                type: "POST",
                url: "http://jsonip.com",
                async: false,
                success: function(res){
                 $( "<p>How am I supposed to know? But your IP is: "+res.ip+"</p>" ).appendTo( ".console_output" );                    
                }
            });
            break;

            case "pwd":
            $( "<p>You are in a future post-apocalypse Earth in the year 2293</p>" ).appendTo( ".console_output" );
            break;

            case "tar":
            $( "<p>tar and feathers are on their way</p>" ).appendTo( ".console_output" );
            break;

            case "apt-get":
            $( "<p>What about trying a real distro like arch or gentoo?</p>" ).appendTo( ".console_output" );
            break;
            
            case "emerge":
            $( "<p>You truly love compiling mate.</p>" ).appendTo( ".console_output" );
            break;
            
            case "yast":
            $( "<p>No fancy GUI for you, do it the hard way.</p>" ).appendTo( ".console_output" );
            break;
            
            case "zypper":
            $( "<p>There are still people out there using SuSE?</p>" ).appendTo( ".console_output" );
            break;

            case "ping":
            $( "<p>Give me a ping, Vasili. One ping only, please.</p>" ).appendTo( ".console_output" );
            break;
            
            case "kill":
            switch(bodycount){
                case 1:
                $( "<p>Doublekill</p>" ).appendTo( ".console_output" );
                bodycount = bodycount+1;
                break;
                
                case 2:
                $( "<p>Triplekill</p>" ).appendTo( ".console_output" );
                bodycount = bodycount+1;
                break;
                
                case 3:
                $( "<p>Multikill</p>" ).appendTo( ".console_output" );
                bodycount = bodycount+1;
                break;
                
                case 4:
                $( "<p><strong>M-M-Monsterkill</strong></p>" ).appendTo( ".console_output" );
                break;
                
                default:
                $( "<p>First blood!</p>" ).appendTo( ".console_output" );
                bodycount = bodycount+1; 
            }
            break;
            
            case "killall":
            $( "<p><strong>M-M-Monsterkill</strong></p>" ).appendTo( ".console_output" );
            break;

            case "inventory":
            $( "<p>You find a old nickel and a much older thuna sandwich in your pockets nothing that will really help you.</p>" ).appendTo( ".console_output" );
            break;
            
            case "wget":
            	if(inputarray.length < 2){
                    $( "<p>Please specify a url</p>" ).appendTo( ".console_output" );
                }   
                else{
                    if(inputarray[1].substr(0, 7) == "http://" || inputarray[1].substr(0, 8) == "https://"){
                    url = inputarray[1]; 
                    }
                    else{
                    url = "http://"+inputarray[1];
                    }            
                }
                
                $.ajax({
                type: "POST",
                url: "/js/php/isup.php",
                data: "isupurl="+url,
                async: false,
                success: function(response){
                    if(response == 200 || response == 301 || response == 302){
                        $( "<p>Open "+url+"</p>" ).appendTo( ".console_output" );
                        $( location ).attr("href", url);
                    }else if (response == 0){
                        $( "<p>Couldn't reach ressource at "+url+"</p>" ).appendTo( ".console_output" );
                    }
                    else{
                        $( "<p>"+url+" returned a Error "+response+"</p>" ).appendTo( ".console_output" );
                    }
                }
            });              	
            break;

            case "hello":
            if(inputarray[1] == "world"){
                $( "<p>Hello you!</p>" ).appendTo( ".console_output" );
            }
            else{
                $( "<p>Hello what?</p>" ).appendTo( ".console_output" );
            }
            break;

            case "go":
            if(inputarray.length < 2){
                $( "<p>Where do you wanna go?</p>" ).appendTo( ".console_output" );
            }   
            else if(inputarray[1] == "north"){
                $( "<p>A dragon appears out of nowhere you're getting instantly killed.</p>" ).appendTo( ".console_output" );
            }   
            else if(inputarray[1] == "east"){
                $( "<p>You're approaching a steep cliff you can't see in the dark and fall of the edge to your certain death.</p>" ).appendTo( ".console_output" );
            }
            else if(inputarray[1] == "south"){
                $( "<p>A angry horde of goblins appears behind a rock, you flee in terror, just to die from a cardiac arrest while running for your life.</p>" ).appendTo( ".console_output" );
            }
            else if(inputarray[1] == "west"){
                $( "<p>You died from dysentery.</p>" ).appendTo( ".console_output" );
            }
            break;

            case "eat":
            if(inputarray.length < 2){
                $( "<p>What do you want to eat?</p>" ).appendTo( ".console_output" );
            } 
            else if(inputarray[1] == "sandwich"){
                $( "<p>You catch salmonella from the old sandwich and die a horrible slow and painfuel death.</p>" ).appendTo( ".console_output" );
            }
            else if(inputarray[1] == "nickel"){
                $( "<p>You can't eat the nickel.</p>" ).appendTo( ".console_output" );
            }
            else{
                $( "<p>There's no "+inputarray[1]+" in your Inventory</p>" ).appendTo( ".console_output" );
            }
            break;
            
            case "use":
            if(inputarray.length < 2){
                $( "<p>What do you want to use?</p>" ).appendTo( ".console_output" );
            } 
            else if(inputarray[1] == "sandwich"){
                $( "<p>You use the sandwich as bait for local wildlife without any sucess.</p>" ).appendTo( ".console_output" );
            }
            else if(inputarray[1] == "nickel"){
                $( "<p>Unfortunely the only vending machine is out of order.</p>" ).appendTo( ".console_output" );
            }
            else{
                $( "<p>There's no "+inputarray[1]+" in your Inventory</p>" ).appendTo( ".console_output" );
            }
            break;

            case "rm":
            if(inputarray[1] == "-rf" && runelevated == 1){
                if($.inArray(inputarray[2], filesystem)!==-1 ){
                    filesystem.splice($.inArray(inputarray[2], filesystem),1);
                }
                else if(inputarray[2] == "/"){
                    $( "<p>Nice try you L33T HAXXXOR ;-)</p>" ).appendTo( ".console_output" );
                }
                else{
                    $( "<p>No such file or directroy</p>" ).appendTo( ".console_output" );
                }
            }
            else if(inputarray[1] == "-rf" && runelevated === 0){
                $( "<p>This command needs elevated privileges</p>" ).appendTo( ".console_output" );
            }
            else{
                if(inputarray[1] == "readme.txt" ){
                    filesystem.splice($.inArray(inputarray[1], filesystem),1);
                }
                else if($.inArray(inputarray[1], filesystem)!==-1 || inputarray[1] == "/"){
                    $( "<p>Cannot delete the directory it contains files or folders use the -rf option</p>" ).appendTo( ".console_output" );
                }
                else{
                    $( "<p>No such file or directroy</p>" ).appendTo( ".console_output" );
                }
            }
            break;

            case "ls":
            if(inputarray.length < 2){
                $.each( filesystem.sort(), function(key, value) {
                    $( "<p>"+value+"</p>" ).appendTo( ".console_output" );
                });
            }
            else if(input == "ls" && $.inArray(inputarray[1], filesystem) !==-1){
                $( "<p>You can't touch this.</p>" ).appendTo( ".console_output" );
            }
            else{
                $( "<p>No such file or directory</p>" ).appendTo( ".console_output" );
            }
            break;

            case "cd":
            baseurl = document.location.hostname;
            if(inputarray.length < 2){
                $( "<p>Where do you wanna go?</p>" ).appendTo( ".console_output" );
            }
            else if(inputarray.length == 2 && $.inArray(inputarray[1], filesystem) !==-1 && inputarray[1] == "readme.txt"){
                $( "<p>You can't list a file use vi or nano instead</p>" ).appendTo( ".console_output" );
            }
            else if(inputarray.length == 2 && $.inArray(inputarray[1], filesystem) !==-1 && inputarray[1] == "/ccc-ch"){
                window.location.replace("http://"+baseurl);
            }
            else if(inputarray.length == 2 && $.inArray(inputarray[1], filesystem) !==-1 && inputarray[1] !== "..."){
                window.location.replace("http://"+baseurl+inputarray[1]+".php");
            }
            else{
                $( "<p>No such file or directroy</p>" ).appendTo( ".console_output" );
            }
            break;

            case "nano":
            case "vi":
            case "emacs":
            if(inputarray[1] == "readme.txt" && $.inArray(inputarray[1], filesystem)!==-1){
                $.get( "/js/readme.txt", function( readme ) {
                    $( "<p>"+readme+"</p>" ).appendTo( ".console_output" );
                });
            }
            else{
                $( "<p>Nothing to edit here...</p>" ).appendTo( ".console_output" );
            }
            break;
            
            default:
            $( "<p>Unrecognized command '"+input+"'. Type 'help' for assistance</p>" ).appendTo( ".console_output" );
        	
        }
        runelevated = 0;
    }
}