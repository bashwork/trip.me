/*
 * wrapper for the tripme api
 */
(function($) {

  var helper = function(root) {
    var base = "http://localhost:8000/api/v1/" + root + '/';

    return {
      all : function(callback) {
        $.getJSON(base, callback);
      },
      get : function(query, callback) {
        $.getJSON(base + 'show/' + query + '/', callback);
      },
      search : function(query, callback) {
        $.getJSON(base + 'search/' + query + '/', callback);
      },
    };
  }

  $.tripme = {
    city    : helper("city"),
    country : helper("country"),
    region  : helper("region"),
    user    : helper("user"),
    spot    : helper("spot"),
    guide   : helper("guide"),
  };

})(jQuery);
