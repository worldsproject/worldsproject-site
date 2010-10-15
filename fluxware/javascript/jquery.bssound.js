$(document).ready(function(){
                             $(document).pngFix();
							 
							 $("a[href$='mp3']").each(function(){
															   href = $(this).attr('href');
														       id = $(this).attr('id');
															   $(this).removeAttr('href');
															   $(this).append('<span>&nbsp;<a href="'+href+'" id="'+id+'Play"><img src="http://www.fluxware.worldsproject.org/images/play.png" style="vertical-align:middle" border="0" /></a>&nbsp;<a href="javascript:stopPlaying(\''+id+'PlayEmbed\');" disabled="disabled"><img src="http://www.fluxware.worldsproject.org/images/stop.png" style="vertical-align:middle" border="0" /></a></span>')
															   });
							 
							 $("a[href$='mp3']").bind('click',function(){																				
														  href = $(this).attr('href');
														  id = $(this).attr('id');
														  $("body").append('<embed id="'+id+'Embed" src="'+href+'" autostart="true" hidden="true"></embed>');
														  return false;
														  });
													
						
													
						   });
function stopPlaying(playID) {
								 
$('#'+playID).remove();
								 
}