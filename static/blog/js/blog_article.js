/*
由于不再使用嵌套的 iframe,这些都没必要了
function getElementTop(element){
　var actualTop = element.offsetTop;
　var current = element.offsetParent;
　while (current !== null){
　　　actualTop += current.offsetTop;
　　　current = current.offsetParent;
　}
　return actualTop;
}


// iframe 高度自适应
function reinitIframe(){
    var iframe = document.getElementById("iframe");
    try{
    var bHeight = iframe.contentWindow.document.body.scrollHeight;
    var dHeight = iframe.contentWindow.document.documentElement.scrollHeight;
    var height = Math.max(bHeight, dHeight);
    iframe.height = height-10;
    }catch (ex){}
}

//生成目录索引列表
function GenerateContentList()
{
    // 花了好久的时间，好气气 ~_~
    var h2=$("#iframe").contents().find("h2");
    var h3=$("#iframe").contents().find("h3");
    // alert(h3.text());
    var iL=h2[0].innerHTML;
    $(".headers").append('<p><b><a href="#TITLE">'+iL+'</a></b></p>');
    var h=getElementTop(h2[0])+130;
    // $('body').append('<div id="TITLE" name="TITLE" style="top:'+h+';position: absolute;color:rgba(0,0,0,0);"'+'>#####</div>');
   
    for(var i=0;i<h3.length;i++){
        var iL=h3[i].innerHTML;
        // $(".headers").append('<p><a href="#header'+i+'">'+iL+'</a></p>');
        $(".headers").append('<p><a onclick="goto_header()" href="#'+iL+'">'+iL+'</a></p>');
        // http://www.ruanyifeng.com/blog/2009/09/find_element_s_position_using_javascript.html
        // var h=getElementTop(h3[i])+130;
        // $('body').append('<div id="header'+i+'" name="header'+i+'" style="top:'+h+';position: absolute;color:rgba(0,0,0,0);"'+'>#####</div>');
    }
    $("#iframe").contents().find("#post-link")[0].innerHTML="<p>本文链接：<a href=' "+window.location.href+" ' class='uri'>"+window.location.href+"</a></p>";
}
*/

function GenerateContentList()
{
    var h2 = $('h2');
    var h3 = $('h3');
    var iL=h2[0].innerHTML;
    $(".headers #insert").append('<li id="first"><b><a target="_self" href="#'+iL+'">'+iL+'</a></b></li>');
    
    for(var i=0;i<h3.length-1;i++){
        var iL=h3[i].innerHTML;
        $(".headers #insert").append('<li><a target="_self" href="#'+iL+'">'+iL+'</a></li>');
    }

    iL=h3[i].innerHTML;
    $(".headers #insert").append('<li id="last"><a target="_self" href="#'+iL+'">'+iL+'</a></li>');
    
    $("#post-link")[0].innerHTML="<p>本文链接：<a href=' "+window.location.href+" ' class='uri'>"+window.location.href+"</a></p>";
}

function header_loc(t){
    var h=$(t).scrollTop();
    if (h>130){
        $('.headers').css("position","fixed");
        $('.headers').css("top","10");
    }
    if (h<120){
        $('.headers').css("position","absolute");
        $('.headers').css("top","120");
    }
}

// http://www.cnblogs.com/iyitong/p/4682859.html
function totop(){
    $('html,body').animate({scrollTop: '0px'}, 800);
}

function todown(){
    $('html,body').animate({scrollTop:$('#bottom').offset().top}, 800);
}