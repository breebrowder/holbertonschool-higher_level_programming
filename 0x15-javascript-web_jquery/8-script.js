$function () {
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
	data.results.forEach(function (i) {
	    $('UL#list_movies').append('<li>${i.title}</li>');
	});
    });
});
