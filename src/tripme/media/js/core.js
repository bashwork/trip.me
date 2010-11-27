/**
 * This redirects a user to the supplied page
 * @param url The page to send the user to
 */
$.redirect = function(url) {
  window.location = url;
};

/*
 * global flag for jquery logging
 */
window.DEBUG = true;

/**
 * This loops through each jquery item and logs it
 * @param this Loops through each instance in this and logs it
 */
$.fn.debug = function() {
  return this.each(function() {
    $.debug(this);
  });
};

/**
 * Logs the passed in message to the browser log
 * @param message The message to log to the browser log
 */
$.debug = function(message) {
  if (window.DEBUG && window.console && window.console.log) {
    window.console.log(message);
  }
};

/*
 * wrapper for the tripme api
 *
 * @author: bashwork at gmail dot com
 * @date: right about now
 * @license: steal and be glad
 */
(function($) {

  var base = "/api/v1/";
  var helper = function(root) {
    var step = base + root + '/';

    return {
      all : function(callback) {
        $.getJSON(step, callback);
      },
      get : function(query, callback) {
        $.getJSON(step + 'show/' + query + '/', callback);
      },
      search : function(query, callback) {
        $.getJSON(step + 'search/' + query + '/', callback);
      },
      remove : function(query, callback) {
        $.ajax({
          type     : 'DELETE',
          url      : step + 'show/' + query + '/',
          success  : callback,
        });
      },
    };
  }

  function markup(data, callback) {
    $.post(base + 'markup/', {data : data }, function(result) {
      if (result.length > 0) {
        callback(result.content);
      } else {
        $.debug(result.content);
      }
    }, "json");
  }

  $.tripme = {
    city    : helper("city"),
    country : helper("country"),
    region  : helper("region"),
    user    : helper("user"),
    spot    : helper("spot"),
    guide   : helper("guide"),
    markup  : markup,
  };

})(jQuery);

/*
 * wrapper for the geonames api
 * http://www.geonames.org/
 *
 * @author: bashwork at gmail dot com
 * @date: right about now
 * @license: steal and be glad
 */
(function($) {

  var base = "http://ws.geonames.org/";

  function _build(name)
  {
    return function(query, callback) {
      $.getJSON(base + name + '?callback=?',
        $.extend({}, $.geonames.options, { q : query }), callback);
    };
  }

  $.geonames = {

    /**
     * member fields
     */
    options : {
      style        : 'full',
      maxRows      : 10,
      featureClass : 'P',
    },

    /**
     * public api
     */
    search : _build('searchJSON'),
    wikipedia : _build('wikipediaSearchJSON'),
    postal : _build('postalCodeSearchJSON'),
    weather : _build('findNearByWeatherJSON'),
  };

})(jQuery);

/*
 * wrapper for the foursquare api
 * http://groups.google.com/group/foursquare-api/web/api-documentation
 *
 * @author: bashwork at gmail dot com
 * @date: right about now
 * @license: steal and be glad
 */
(function($) {

  $.foursquare = {};
  var base = "/api/v1/proxy/foursquare/";
  //var base = "https://api.foursquare.com/v1/";
  var options = { l : 30, };

  function convert_options(query)
  {
    var result = {
      geolat  : query.lat,
      geolong : query.lng,
    };
    if (query.search) {
      result.q = query.search;
    }
    return result;
  }

  $.foursquare.venue = {
    /**
     */
    get : function(id, callback) {
      $.getJSON(base + 'venue.json?callback=?',
        { vid : id }, callback);
    },

    /**
     */
    search : function(query, callback) {
      $.getJSON(base + 'venues.json?callback=?',
        $.extend({}, options, convert_options(query)), callback);
    },
  };

  $.foursquare.tips = {
    /**
     */
    near : function(query, callback) {
      $.getJSON(base + 'tips.json?callback=?',
        $.extend({}, options, convert_options(query),
          { filter : 'nearby' }), callback);
    },
  };

  /**
   */
  $.foursquare.categories = function(callback) {
    $.getJSON(base + 'categories.json?callback=?', callback);
  };

  /**
   */
  $.foursquare.test = function(callback) {
    $.getJSON(base + 'test.json?callback=?', callback);
  };


  function process_result(result)
  {
    var venues = (result.groups.length > 0)
      ? result.groups[0].venues : {};
    var list = $.map(venues, function(venue) {
      return '<article class="spot-summary clearfix">'
        + '<h1>' + venue.name + '</h1>'
        + '<a href="/venue/' + venue.id + '"/ class="button">+ add to guide</a>'
        //+ '<img src="' + (venue.primarycategory) ? venue.primarycategory.iconurl : '' + '" height="150px" />'
        + '<p>getting there</p>'
        + '</article>';
    });

    return list.join('');
  }  

  /**
   * jquery api
   */
  $.fn.foursquare = function(options) {
    return this.each(function() {
      $this = $(this);
      $.foursquare.venue.search(options, function(data) {
        $this.append(process_result(data));
      });
    });
  };

})(jQuery);

/**
 * jquery.gmaps v3
 * http://code.google.com/apis/maps/documentation/javascript/basics.html
 *
 * @url     http://www.pittss.lv/jquery/gomap/
 * @author  Galen Collins
 * @version 1.0
 */
(function($) {
 /**
  * If we don't have google maps api loaded, no
  * sense in continuing
  */
 if (!window.google) { return; }

 //var Gmaps = function(opts) {
 //  this.options = $.extend({}, $.fn.gmaps.defaults, options);
 //  this.geocoder = new google.maps.Geocoder();
 //};
 var G = {}
 $.gmaps = {};

 $.fn.gmaps = function(options) {

     return this.each(function() {

         var opts = $.extend({}, $.gmaps.defaults, options);
         //var element = $(this);
         //if (element.data('gmaps')) { return; }
         //var plugin = new gmaps(this, opts);
         //element.data('gmaps', plugin);

         G = {
           id      : this,
           options : opts,
           markers : [],
           center  : null,
         };
         $.gmaps.init(opts);
     });
 };

 $.gmaps.defaults = {
   center                   : [39.50, -98.35],
   zoom                     : 3,
   maptype                  : 'roadmap',
   disableDoubleClickZoom   : true,
   mapTypeControl           : false,
   streetViewControl        : false,
   mapTypeControlOptions    : {
     style                  : 'default',
     position               : 'top_right',
   },
   navigationControl        : true,
   navigationControlOptions : {
     style                  : 'small',
     position               : 'top_left',
   },
   scaleControl             : false,
   scrollwheel              : true,
   prefix                   : 'gmarker',
   markers                  : [],
 };

 /**
  * wrapper around the google maps constants
  */
 var gapi = (function() {

   function get(result, set) {
     return function(value) {
       value = value.toUpperCase();
       return set[value in set ? value : result];
     }
   }
   
   function get_ll(area) {
     return new google.maps.LatLng(area[0], area[1]);
   }

   function get_options(opts) {
     return {
       //center                   : this.centerLatLng,
       disableDoubleClickZoom   : opts.disableDoubleClickZoom,
       streetViewControl        : opts.streetViewControl,
       mapTypeControl           : opts.mapTypeControl,
       mapTypeControlOptions    : {
         style    : gapi.typeStyle(opts.mapTypeControlOptions.style),
         position : gapi.typePosition(opts.mapTypeControlOptions.position),
       },
       mapTypeId                : gapi.mapType(opts.maptype),
       navigationControl        : opts.navigationControl,
       navigationControlOptions : {
         style    : gapi.navStyle(opts.navigationControlOptions.style),
         position : gapi.navPosition(opts.navigationControlOptions.position),
       },
       scaleControl             : opts.scaleControl,
       scrollwheel              : opts.scrollwheel,
       zoom                     : opts.zoom,
     };
   }

   var geocoder = new google.maps.Geocoder();

   return {
     mapType      : get('ROADMAP', google.maps.MapTypeId),
     typeStyle    : get('DEFAULT', google.maps.MapTypeControlStyle),
     typePosition : get('TOP_RIGHT', google.maps.ControlPosition),
     navStyle     : get('DEFAULT', google.maps.NavigationControlStyle),
     navPosition  : get('TOP_LEFT', google.maps.ControlPosition),
     latlng       : get_ll,
     options      : get_options,
     geocode      : geocoder.geocode,
     infowindow   : new google.maps.InfoWindow(),
   };
 })();

 /**
  */
 $.gmaps.init = function(opts) {
   G.map = new google.maps.Map(G.id, gapi.options(opts));
   $.gmaps.center(opts.center);

   for (var i = 0; i < opts.markers.length; ++i) {
     $.gmaps.mark(opts.markers[i]);
   }

   //$.gmaps.bind('click', function(ev) {
   //  var mark = $.gmaps.mark({
   //    position  : ev.latLng,
   //    draggable : true,
   //  });
   //});
   return this;
 };

 /**
  */
 $.gmaps.update = function(opts) {
   var current = $.extend(G.options, opts);
   G.map.setOptions(gapi.options(current));
   return this;
 }

 /**
  */
 $.gmaps.bind = function(ev, fn, source) {
   google.maps.event.addListener(
     source ? source : G.map, ev, fn);
   return this;
 };

 /**
  */
 $.gmaps.unbind = function(ev, source) {
   google.maps.event.removeListener(
     source ? source : G.map, ev);
   return this;
 };

 /**
  */
 $.gmaps.center = function(area) {
    if ($.isArray(area) && (area.length == 2)) {
      G.center = gapi.latlng(area);
      G.map.setCenter(G.center);
    } else if (typeof(area) == 'string') {
      return $.gmaps.geocode(area, $.gmaps.center);
    } else if (G.markers[0]) {
      $.gmaps.center(G.markers[0].area);
    }
   return this;
 };

 function add_info_window(marker)
 {
   $.gmaps.bind('click', function() {
     gapi.infowindow.setContent(marker.content);
     gapi.infowindow.open(G.map, marker);  
   }, marker);
 }

 /**
  * title, visible, id, icon, 
  */
 $.gmaps.mark = function(marker, move) {
    
   if ($.isArray(marker.position) && (marker.position.length == 2)) {
     marker.position = gapi.latlng(marker.position);
   } else if (marker.position && marker.position.lat && marker.position.lng) {
     // looks good to me
   } else if (typeof(marker.position) == 'string') {
     return $.gmaps.geocode(marker.position, function (po) {
       $.gmaps.mark($.extend(marker, { position: po }), move);
     });
   } else {
     $.debug("invalid position type for marker");
   }

   var opts = $.extend({
     map       : G.map,
     id        : G.options.prefix + G.markers.length,
     draggable : false,
   }, marker);
   var marker = new google.maps.Marker(opts);

   if (move) {
     G.map.panTo(marker.position);
   }

   if (marker.content) {
     add_info_window(marker);
   }

   $(G.id).data(marker.id, marker);
   G.markers.push(marker.id);
   return this;
 };

 /**
  */
 $.gmaps.markers = function() {
   var results = [], H = $(G.id);
   
   for (var i in G.markers) {
     results[i] = H.data(G.markers[i]);
   }
   return results;
 };

 function delete_marker(id) {
   var marker  = $(G.id).data(id);
   marker.setVisible(false);
   marker.setMap(null);
   $(G.id).removeData(id);
   // remove info window
 }

 /**
  */
 $.gmaps.unmark = function(marker) {
   var index = $.inArray(marker, G.markers);
   if (index > -1) {
     var current = G.markers.split(index, 1);
     delete_marker(current[0]);
   }
   //return (index > -1);
   return this;
 };

 /**
  */
 $.gmaps.unmarkAll = function(marker) {
   for (var i in G.markers) {
     delete_marker(G.markers[i]);
   }
   G.markers = [];
   return this;
 };

 /**
  */
 $.gmaps.refit = function(area) {
   return this;
 };

 /**
  */
 $.gmaps.geocode = function(address, callback, errback) {
   gapi.geocode({ 'address': address }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        callback(results[0].geometry.location);
      } else {
        $.debug(status);
        if (errback) { errback(status); }
      }
   });
   return this;
 };

 /**
  */
 $.gmaps.geodecode = function(area, callback, errback) {
   gapi.geocode({ 'latLng': area }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        callback(results[0].formatted_address);
      } else {
        $.debug(status);
        if (errback) { errback(status); }
      }
   });
   return this;
 };
})(jQuery);

/**
 * jQuery flickr
 * http://www.flickr.com/services/api/
 *
 * @author: bashwork at gmail dot com
 * @date: right about now
 * @license: steal and be glad
 */
(function($) {

  /**
   * private api
   */
  var flickr = {
    /**
     * member fields
     */
    base    : 'http://api.flickr.com/services/rest/',
    options : {
      format       : 'json',
      api_key      : '4d67f7aabdf16f65f66b0e4242823334',
      accuracy     : 10, // at least city
      safe_search  : 1,  // no porn
      class        : 'flickr',
      size         : 's',
      content_type : 1,  // just photos
      // text      : '',
      // tags      : '',
      // per_page  : 1,
      // page      : 1,
    },

    /**
     * a helper method to convert a reasonable size
     * value to flickr's version
     */
    get_size : function(size) {
      switch(size) {
        case 'sq': return '_s' // square
        case 't' : return '_t' // thumbnail
        case 's' : return '_m' // small
        case 'm' : return ''   // medium
        case 'ml': return '_z' // medium large
        case 'l' : return '_b' // large
        default  : return '_m' // small
      }
    },

    /**
     * http://farm{farm-id}.static.flickr.com/{server-id}/{id}_{secret}.jpg
     * http://farm{farm-id}.static.flickr.com/{server-id}/{id}_{secret}_[mstzb].jpg
     * http://farm{farm-id}.static.flickr.com/{server-id}/{id}_{o-secret}_o.(jpg|gif|png)
     */
    get_url : function (photo, size) {
      return ["http://farm", photo.farm, ".static.flickr.com/",
        photo.server, "/", photo.id, "_", photo.secret,
        flickr.get_size(size), ".jpg"].join('');
    },

    get_img : function (image) {
      return ['<img src="', image.src,
        '" alt="', image.alt, '" />'].join('');
    },

    /**
     * accepts a series of photos and constructs
     * the thumbnails that link back to Flickr
     */
    process : function(photos, options) {
      var thumbnails = $.map(photos.photo, function(photo) {
        var image = new Image(), html = '';

        image.src = flickr.get_url(photo, options.size)
        image.alt = photo.title
          
        return ['<li>' + flickr.get_img(image) + '</li>']
      }).join("\n")
      
      return $('<ul>').addClass(options.class).append(thumbnails)
    },

    /**
     * perform the actual request and process
     * the resulting images
     */
    request : function(query, method, callback) {
      var opts = $.extend(flickr.options, query, { method : method });
      $.getJSON(flickr.base + '?jsoncallback=?', opts, function(data) {
        if (data.stat == 'ok') {
          var photos = (data.photos === undefined)
            ? data.photoset : data.photos;
          callback(flickr.process(photos, opts));
        } else { $.debug(data); }
      });
    },
  };

  function _build(method) {
    return function(query, callback) {
      flickr.request(query, method, callback);
    }
  }

  /**
   * public api
   * for most of these, you may have to look up the
   * parameters...sorry.
   */
  $.flickr = {
    search      : _build('flickr.photos.search'),
    recent      : _build('flickr.photos.getRecent'),
    photoset    : _build('flickr.photosets.getPhotos'),
    interesting : _build('flickr.interestingness.getList'),
    username    : _build('flickr.people.getPublicPhotos'),
    contacts    : _build('flickr.photos.getContactsPublicPhotos'),
    lookup      : _build('flickr.people.FindByUsername'),
  };

  /**
   * jquery api
   */
  $.fn.flickr = function(options) {
    return this.each(function() {
      $this = $(this);
      $.flickr.search(options, function(data) {
        $this.append(data);
      });
    });
  };

})(jQuery);
