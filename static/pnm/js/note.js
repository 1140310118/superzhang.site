
function functions_for_new_note_to_bind(note_id){
	$('#note_'+note_id+' textarea').change(function(){
		modify_note_by_id(note_id); });
	$('#note_'+note_id+' button').click(function(){
		delete_note_by_id(note_id); });
	$('#note_'+note_id+' textarea').focus(function(){
		focus_outline(this)});
	$('#note_'+note_id+' textarea').blur(function(){
		blur_outline(this)});
	$('#note_'+note_id+' .note_top').mousedown(function(e){
		note_top_mousedown(e,this); }); }
// 移动
// 参考：http://blog.sina.com.cn/s/blog_7d12ba3f01014fz5.html
function note_top_mouseup(w){
	$(".note_top").css("cursor","default");
	$(w).unbind('mousemove'); }
function note_top_mousedown(e,w){
	$(w).css("cursor","move");
	var offset = $(w).parent().offset();
	var x=e.pageX - offset.left;
	var y=e.pageY - offset.top;
	var note_div_id = $(w).parent().attr("id");
	$(document).mousemove(function(ev){
		$(".note_top").stop();
		var _x=ev.pageX - x;
		var _y=ev.pageY - y;
		$("#"+note_div_id).animate({left:_x+"px",top:_y+"px"},10); }); }
function move_with_mouse(note_id){
	$('.note_top').mousemove(function(e){
		last_x=e.pageX;
		last_y=e.pageY;
		offset_x=e.pageX-last_x;
		offset_y=e.pageY-last_y;
		$("span").text(offset_x + ", " + offset_y); }); }
// focus效果
function focus_outline(w){
	$(w).parent().css("outline","1px solid rgb(51,133,255)");}
function blur_outline(w){
	$(w).parent().css("outline","none");}

// 修改笔记
function modify_note_by_id(note_id){
	content=$("#note_"+note_id+" textarea").val();
	$.post("/_modify_note/",{'note_id': note_id,'content': content});
}
// 删除笔记
function delete_note_by_id(note_id){
	$("#note_"+note_id).hide();
	$.post("/_delete_note/",{'note_id': note_id});
}