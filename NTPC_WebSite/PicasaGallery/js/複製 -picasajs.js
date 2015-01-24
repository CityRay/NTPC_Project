// Picasa Gallery Show by Ray

function  getpicasa(id,idiv, textchange){
	
	var name = "107831722258936432290";
	var numi = 1;
	var number = 0;
	$.getJSON("https://picasaweb.google.com/data/feed/api/user/"+name+"/albumid/"+id+"?alt=json&callback=?",function(json){	
		$(json.feed.entry).each(function (i, item){
			var title = item.title.$t;
			var ghpotoid = item.gphoto$albumid.$t; //相簿的id
			var photoid = item.gphoto$id.$t; //相片的id
			
			
   			 //var url = item.media$group.media$thumbnail[0].url;//這也是縮圖，但太小了
			 
  			 var href = item.link[0].href+"&callback=?";
			 
			 var psrc = item.content.src + '?imgmax=160' ;
 			 var bsrc = item.content.src;
			
			 var aldec = item.media$group.media$description.$t; //相片的文字說明
	
										 
	
		if(i == 0 )
		{
			
		$(idiv).empty();		
		$(idiv).append("<div class='itemsc'><div class='thumb'><a href=https://plus.google.com/photos/107831722258936432290/albums/" + ghpotoid+"/"+photoid + " target='_blank'><img src='" + psrc + "'/></a><br><p class='" + textchange + "'><a href=https://plus.google.com/photos/107831722258936432290/albums/" + ghpotoid+"/"+photoid + " target='_blank'>" + aldec +"</a></p></div></div>");

		$("'." + textchange + "'").limitstring(ghpotoid, photoid);
		//$("[@limit]").limitstring();
		
		}
		
		});	
		});
	
	return false;

}

(function($){	
		  
	var dclass = '';
	var ctext = '';
	
	for(nmi = 1; nmi<6 ; nmi++)
	{
	
	if(nmi == 1)
	{
		albumid = "5711470630134940545";
		
		dclass = '#item1';	
		ctext = 'text1';
		
		getpicasa(albumid, dclass, ctext);
		
	}else if(nmi == 2){
		albumid = "5711470428077566417";
		
		dclass = '#item2';		
		ctext = 'text2';
		getpicasa(albumid, dclass, ctext);
		
	}else if(nmi == 3){
		albumid = "5711470296917256097";
		
		dclass = '#item3';		
		ctext = 'text3';
		getpicasa(albumid, dclass, ctext);
		
	}else if(nmi == 4){
		albumid = "5711470131658269409";
		
		dclass = '#item4';		
		ctext = 'text4';
		getpicasa(albumid, dclass, ctext);
		
	}else {
		albumid = "5711469966903581185";
		
		dclass = '#item5';	
		ctext = 'text5';
		getpicasa(albumid, dclass, ctext);
		
	}
	//window.alert("NUMER_end"+nmi);	
	}
	
	

return false;

})(jQuery);


jQuery.fn.limitstring=function(ghpotoid, photoid)
{
	var objString = $(this).text();
	var objLength = $(this).text().length;
	
	if(objLength > 20)
	{
		
		$(this).attr("title",objString);
		objString = $(this).html("<a href=https://plus.google.com/photos/107831722258936432290/albums/" + ghpotoid+"/"+photoid + " target='_blank'>" + objString.substring(0,20) + "</a>...");

	}
	
}

