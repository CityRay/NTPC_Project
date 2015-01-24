// Picasa Gallery Show by Ray

function  getpicasa(id, idiv, textchange){
	
	var name = "107831722258936432290";
	var numi = 1;
	var number = 0;
	
	//https://picasaweb.google.com/data/feed/api/user/107831722258936432290/albumid/5711470630134940545?alt=json&callback=?
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
		$(idiv).append("<div class='itemsc' class='clearfix'><div class='thumb'><a href=https://picasaweb.google.com/107831722258936432290/" + textchange +"#" +photoid+ " target='_blank'><img src='" + psrc + "'/></a></div><p class='" + textchange + "'><a href=https://picasaweb.google.com/107831722258936432290/" + textchange+"#"+photoid + " target='_blank'>" + aldec +"</a></p></div>");
		
		

		var chtext = "." + textchange;
		
		$(chtext).limitstring(ghpotoid, photoid, textchange);
		

		
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
		ctext = 'Test10';
		
		getpicasa(albumid, dclass, ctext);
		
	}else if(nmi == 2){
		albumid = "5711470428077566417";
		
		dclass = '#item2';		
		ctext = 'Test9';
		getpicasa(albumid, dclass, ctext);
		
	}else if(nmi == 3){
		albumid = "5711470296917256097";
		
		dclass = '#item3';		
		ctext = 'Test8';
		getpicasa(albumid, dclass, ctext);
		
	}else if(nmi == 4){
		albumid = "5711470131658269409";
		
		dclass = '#item4';		
		ctext = 'Test7';
		getpicasa(albumid, dclass, ctext);
		
	}else {
		albumid = "5711469966903581185";
		
		dclass = '#item5';	
		ctext = 'Test6';
		getpicasa(albumid, dclass, ctext);
		
	}

	}
	
	

return false;

})(jQuery);


jQuery.fn.limitstring=function(ghpotoid, photoid, textchange)
{
	var objString = $(this).text();
	var objLength = $(this).text().length;

	
	if(objLength > 20)
	{

		$(this).attr("title",objString);
		objString = $(this).html("<a href=https://picasaweb.google.com/107831722258936432290/" + textchange +"#"+photoid + " target='_blank'>" + objString.substring(0,20) + "</a>...");

	}
	
}

