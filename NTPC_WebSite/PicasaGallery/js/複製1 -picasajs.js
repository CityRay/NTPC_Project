// Picasa Gallery Show by Ray
function  getpicasa(id,idiv){
	
	var name = "107831722258936432290";
	var numi = 1;
	var number = 0;
	$.getJSON("https://picasaweb.google.com/data/feed/api/user/"+name+"/albumid/"+id+"?alt=json",function(json){	
		$(json.feed.entry).each(function (i, item){
			var title = item.title.$t;
   			 var url = item.media$group.media$thumbnail[0].url;
  			 var href = item.link[0].href+"&callback=?";
			var psrc = item.content.src + '?imgmax=160' ;
 			var bsrc = item.content.src + '?imgmax=800';
			var ptt = item.media$group.media$title.name;
			var aldec = item.media$group.media$description.$t;
			var thurl = item.url; 
										 
	
		if(i == 0 )
		{
		$(idiv).append("<div class='itemsc'><div class='thumb'><a href='" + bsrc + "'><img src='" + psrc + "'/></a><br />" + aldec +"</div></div>");
		}
		});	
		});
	
	return false;

}

(function($){	
		  
	var dclass = ''
	
	for(nmi = 1; nmi<6 ; nmi++)
	{
	
	if(nmi == 1)
	{
		albumid = "5711470630134940545";
		
		dclass = '#item1';		
		getpicasa(albumid, dclass);
		
	}else if(nmi == 2){
		albumid = "5711470428077566417";
		
		dclass = '#item2';		
		getpicasa(albumid, dclass);
		
	}else if(nmi == 3){
		albumid = "5711470296917256097";
		
		dclass = '#item3';		
		getpicasa(albumid, dclass);
		
	}else if(nmi == 4){
		albumid = "5711470131658269409";
		
		dclass = '#item4';		
		getpicasa(albumid, dclass);
		
	}else {
		albumid = "5711469966903581185";
		
		dclass = '#item5';		
		getpicasa(albumid, dclass);
		
	}
	//window.alert("NUMER_end"+nmi);	
	}

return false;

})(jQuery);



 