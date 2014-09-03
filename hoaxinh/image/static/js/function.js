$(document).ready(function(){
   
   /* Top menu add photo click event */
   $('#add-photos-btn').click(function(e){
       e.preventDefault();

       // select images
       $('input#add-photos').click();
   });

   /* Ajax upload photos */
   $('input#add-photos').on('change', function(){
   		
   		// set files from input
   		var files = this.files;

   		// create js form for upload photos
   		var formData = new FormData();
   		for(i=0; i < files.length; i++){
        var ext = files[i].name.split('.').pop().toLowerCase();
        if($.inArray(ext, ['gif','png','jpg','jpeg']) == -1) {
            alert('Ảnh mới up được em ơi ^_^!');
        }else{
   			    formData.append('files[]', files[i]);
        }
   		}
   		formData.append('csrfmiddlewaretoken', csrftoken);
   		console.log(formData);

         // Show loading animation
         progressBar = new $.Progress();
         progressBar.show();
   		$.ajax({
   			url: '/image/add/',
   			type: 'POST',
   			dataType: 'json',
   			data: formData,
   			processData: false,
   			contentType: false,
            xhr: function(){
               var xhr = new window.XMLHttpRequest();
               // Upload progress
               xhr.upload.addEventListener('progress', function(e){
                  if(e.lengthComputable){
                     var percent = e.loaded/e.total;
                     progressBar.setPercentage(percent*100);
                  }
               }, false);
               return xhr;
            },
   			success: function(data){
   				console.log(data)
               // Hide progress bar
               progressBar.hide();
               // Redirect to list photos page
               window.location.href = '/image/list/';
   			},
   			error: function(data){
   				console.log('error');
   				console.log(data);
   			},
   		});
   });
   
   /* Ajax clear photos */
   $('a#clear-photos').click(function(e){
      e.preventDefault();

      $.ajax({
         url: $(this).attr('href'),
         type: 'POST',
         data: {
            csrfmiddlewaretoken: csrftoken,
         },
         success: function(){
            // Redirect to list photos page
            window.location.href = '/image/list/';
         },
         error: function(){
            alert('error');
         },
      });
   });
});

/* Progress function */
(function($){
   $.Progress = function(){

   };

   $.Progress.prototype = {
      show: function(){
         if(!$('#progress-bar').length){
            $('body').append('<div id="progress-bar"><div class="peg"></div></div>');
         }
         $('#progress-bar').show();
      },
      setPercentage: function(percent){
         $('#progress-bar').css('transition', 'all 200ms ease');
         $('#progress-bar > div').css('width', percent + '%');
      },
      hide: function(){
         $('#progress-bar').hide();
         $('#progress-bar > div').css('width', 0);
      },
   };
})(jQuery);

/* Get crsf token function */
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Global csrf token
var csrftoken = getCookie('csrftoken');