/**
 * debug
 * This loops through each jquery item and logs it
 */
$.redirect = function(url) {
  window.location = url;
};

/*
 * global flag for jquery logging
 */
window.DEBUG = true;

/**
 * debug
 * This loops through each jquery item and logs it
 */
$.fn.debug = function() {
  return this.each(function() {
    $.debug(this);
  });
};

/**
 * debug
 * Logs the passed in message to the browser log
 */
$.debug = function(message) {
  if (window.DEBUG && window.console && window.console.log) {
    window.console.log(message);
  }
};

/*
 * wrapper for the tripme api
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
 * wrapper for the foursquare api
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
        $.extend(options, convert_options(query)), callback);
    },
  };

  $.foursquare.tips = {
    /**
     */
    near : function(query, callback) {
      $.getJSON(base + 'tips.json?callback=?',
        $.extend(options, convert_options(query),
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

})(jQuery);

/**
 * jquery.gmaps v3
 *
 * @url     http://www.pittss.lv/jquery/gomap/
 * @author  Galen Collins
 * @version 1.0
 */
(function($) {

 /**
  * default configuration options and globals
  */
 var geocoder = new google.maps.Geocoder();
 var infowindow = new google.maps.InfoWindow();
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

   return {
     mapType      : get('ROADMAP', google.maps.MapTypeId),
     typeStyle    : get('DEFAULT', google.maps.MapTypeControlStyle),
     typePosition : get('TOP_RIGHT', google.maps.ControlPosition),
     navStyle     : get('DEFAULT', google.maps.NavigationControlStyle),
     navPosition  : get('TOP_LEFT', google.maps.ControlPosition),
     latlng       : get_ll,
     options      : get_options,
   };
 })();

 /**
  */
 $.gmaps.init = function(opts) {
   G.map = new google.maps.Map(G.id, gapi.options(opts));
   $.gmaps.center(opts.center);

   for (i = 0; i < opts.markers.length; ++i) {
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
   var current = $.extend({}, G.opts, opts);
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
     infowindow.setContent(marker.content);
     infowindow.open(G.map, marker);  
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
   
   for (i in G.markers) {
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
   for (i in G.markers) {
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
   geocoder.geocode({ 'address': address }, function(results, status) {
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
   geocoder.geocode({ 'latLng': area }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        callback(results[0].formatted_address);
      } else {
        $.debug(status);
        if (errback) { errback(status); }
      }
   });
   return this;
 };

/**
 * jQuery flickr
 * https://github.com/rpheath/jquery-flickr/blob/master/jquery.flickr.js
 */
(function($) {

  var base = 'http://api.flickr.com/services/rest/';

  function convert_options(query)
  {
    var result = {
      lat : query.lat,
      lon : query.lng,
    };
    return result;
  }

  $.flickr = {
    /**
     */
    options : {
      format  : 'json',
      api_key : '802e2bd0c4f71377d5301a9638446104',
      method  : 'flickr.photos.geo.photosForLocation',
    },

    /**
     */
    search : function(query, callback) {
      $.getJSON(base + '?jsoncallback=?',
        $.extend($.flickr.options, convert_options(query)), function(data) {
          if (data.stat == 'ok') {
            callback(data);
          } else { $.debug(data); }
      });
    },
  };

  /**
   */
  $.fn.flickr = function(options) {
      return this.each(function() {
        var ul = $('<ul>').appendTo(this);
        $.flickr.search(options, function(data) {
          // do the things
        });
      });
  };

})(jQuery);

/**
 * jQuery goMap
 *
 * @url     http://www.pittss.lv/jquery/gomap/
 * @author  Jevgenijs Shtrauss <pittss@gmail.com>
 * @version 1.2.1
 * This software is released under the MIT License <http://www.opensource.org/licenses/mit-license.php>
 */

(function($) {
    var geocoder = new google.maps.Geocoder();

    function MyOverlay(map) { this.setMap(map); };
    MyOverlay.prototype = new google.maps.OverlayView();
    MyOverlay.prototype.onAdd = function() { };
    MyOverlay.prototype.onRemove = function() { };
    MyOverlay.prototype.draw = function() { };

    $.fn.goMap = function(options) {
        var opts = $.extend({}, $.goMap.defaults, options);

        return this.each(function() {
            $.goMap.mapId        = this;
            $.goMap.opts         = opts;
            $.goMap.markers      = [];
            $.goMap.centerLatLng = null;
            $.goMap.init(opts);
        });
    };

    $.goMap = {
        defaults: {
            address:                '', // Street, City, Country
            latitude:               56.9,
            longitude:              24.1,
            zoom:                   4,
            delay:                  500,
            hideByClick:            true,
            oneInfoWindow:          true,
            prefixId:               'gomarker',
            navigationControl:      true, // Show or hide navigation control
            navigationControlOptions: {
                position:           'TOP_LEFT', // TOP, TOP_LEFT, TOP_RIGHT, BOTTOM, BOTTOM_LEFT, BOTTOM_RIGHT, LEFT, RIGHT
                style:              'DEFAULT' // DEFAULT, ANDROID, SMALL, ZOOM_PAN
            },
            mapTypeControl:         true, // Show or hide map control
            mapTypeControlOptions:  {
                position:           'TOP_RIGHT', // TOP, TOP_LEFT, TOP_RIGHT, BOTTOM, BOTTOM_LEFT, BOTTOM_RIGHT, LEFT, RIGHT
                style:              'DEFAULT' // DEFAULT, DROPDOWN_MENU, HORIZONTAL_BAR
            },
            scaleControl:           false, // Show or hide scale
            scrollwheel:            true, // Mouse scroll whell
            directions:             false,
            directionsResult:       null,
            disableDoubleClickZoom: false,
            streetViewControl:      false,
            markers:                [],
            maptype:                'ROADMAP', // Map type - HYBRID, ROADMAP, SATELLITE, TERRAIN
            html_prepend:           '<div class=gomapMarker>',
            html_append:            '</div>',
            addMarker:              false
        },

        map:          null,
        count:        0,
        markers:      [],
        bounds:       null,
        overlay:      null,
        mapId:        null,
        opts:         null,
        centerLatLng: null,

        init: function(opts) {
            if (opts.address)
                $.goMap.geocode(opts.address, true);

            else if (opts.latitude != this.defaults.latitude && opts.longitude != this.defaults.longitude)
                this.centerLatLng = new google.maps.LatLng(opts.latitude,opts.longitude);

            else if ($.isArray(opts.markers) && opts.markers.length > 0) {
                if (opts.markers[0].address)
                    $.goMap.geocode(opts.markers[0].address, true);
                else
                    this.centerLatLng = new google.maps.LatLng(opts.markers[0].latitude,opts.markers[0].longitude);
            }
            else
                this.centerLatLng = new google.maps.LatLng(opts.latitude,opts.longitude);

            var myOptions = {
                center:                 this.centerLatLng,
                disableDoubleClickZoom: opts.disableDoubleClickZoom,
                mapTypeControl:         opts.mapTypeControl,
                streetViewControl:      opts.streetViewControl,
                mapTypeControlOptions:  {
                    position:           eval('google.maps.ControlPosition.' + opts.mapTypeControlOptions.position.toUpperCase()),
                    style:              eval('google.maps.MapTypeControlStyle.' + opts.mapTypeControlOptions.style.toUpperCase())
                },
                mapTypeId:              eval('google.maps.MapTypeId.' + opts.maptype.toUpperCase()),
                navigationControl:      opts.navigationControl,
                navigationControlOptions: {
                    position:           eval('google.maps.ControlPosition.' + opts.navigationControlOptions.position.toUpperCase()),
                    style:              eval('google.maps.NavigationControlStyle.' + opts.navigationControlOptions.style.toUpperCase())
                },
                scaleControl:           opts.scaleControl,
                scrollwheel:            opts.scrollwheel,
                zoom:                   opts.zoom
            };

            $.goMap.map     = new google.maps.Map(this.mapId, myOptions);
            $.goMap.overlay = new MyOverlay($.goMap.map);

            for (var j = 0; j < opts.markers.length; j++)
                this.createMarker(opts.markers[j]);

            if (opts.addMarker == true || opts.addMarker == 'multi') {
                google.maps.event.addListener($.goMap.map, 'click', function(event) {
                    var options = {
                        position:  event.latLng,
                        draggable: true
                    };
                    var marker = $.goMap.createMarker(options);

                    google.maps.event.addListener(marker, 'dblclick', function(event) {
                        marker.setMap(null);
                        $.goMap.removeMarker(marker.id);
                    });

                });
            }
            else if (opts.addMarker == 'single') {
                google.maps.event.addListener($.goMap.map, 'click', function(event) {
                    if(!$.goMap.singleMarker) {
                        var options = {
                            position:  event.latLng,
                            draggable: true
                        };
                        var marker = $.goMap.createMarker(options);

                        $.goMap.singleMarker = true;

                        google.maps.event.addListener(marker, 'dblclick', function(event) {
                            marker.setMap(null);
                            $.goMap.removeMarker(marker.id);
                            $.goMap.singleMarker = false;
                        });
                    }
                });
            }
        },

        getMap: function() {
           return $.goMap.map;
        },

        setMap: function(options) {
            delete options.mapTypeId;

            if (options.address) {
                $.goMap.geocode(options.address, true);
                delete options.address;
            }
            else if (options.latitude && options.longitude) {
                options.center = new google.maps.LatLng(options.latitude,options.longitude);
                delete options.longitude;
                delete options.latitude;
            }

            if(options.mapTypeControlOptions && options.mapTypeControlOptions.position)
                options.mapTypeControlOptions.position = eval('google.maps.ControlPosition.' + options.mapTypeControlOptions.position.toUpperCase());

            if(options.mapTypeControlOptions && options.mapTypeControlOptions.style)
                options.mapTypeControlOptions.style = eval('google.maps.MapTypeControlStyle.' + options.mapTypeControlOptions.style.toUpperCase());

            if(options.navigationControlOptions && options.navigationControlOptions.position)
                options.navigationControlOptions.position = eval('google.maps.ControlPosition.' + options.navigationControlOptions.position.toUpperCase());

            if(options.navigationControlOptions && options.navigationControlOptions.style)
                options.navigationControlOptions.style = eval('google.maps.NavigationControlStyle.' + options.navigationControlOptions.style.toUpperCase());

            $.goMap.map.setOptions(options);
        },

        createListener: function(type, event, data) {
            var target;

            if(typeof type != 'object')
                type = {type:type};

            if(type.type == 'map')
                target = $.goMap.map;
            else if(type.type == 'marker' && type.marker)
                target = $(this.mapId).data(type.marker);
            else if(type.type == 'info' && type.marker)
                target = $(this.mapId).data(type.marker + 'info');

            if(target)
                return google.maps.event.addListener(target, event, data);
        },

        removeListener: function(listener) {
            google.maps.event.removeListener(listener);
        },

        geocode: function(address, setCenter, options) {
            setTimeout(function() {
                geocoder.geocode({'address': address}, function(results, status) {

                    if (status == google.maps.GeocoderStatus.OK && setCenter)
                        $.goMap.map.setCenter(results[0].geometry.location);

                    if (status == google.maps.GeocoderStatus.OK && options && options.markerId)
                        options.markerId.setPosition(results[0].geometry.location);

                    else if (status == google.maps.GeocoderStatus.OK && options) {
                        options.position = results[0].geometry.location;
                        var cmarker = new google.maps.Marker(options);

                        if (options.html) {
                            if (!options.html.content && !options.html.ajax && !options.html.id)
                                options.html = { content:options.html };
                            else if (!options.html.content)
                                options.html.content = null;

                            $.goMap.setInfoWindow(cmarker, options.html);
                        }
                        $.goMap.addMarker(cmarker);
                        return cmarker;
                    }

                    else if(status == google.maps.GeocoderStatus.OVER_QUERY_LIMIT) {
                        $.goMap.geocode(address, false, options);
                    }
                });
            }, this.opts.delay);
        },

        setInfoWindow: function(marker, html) {
            html.content    = this.opts.html_prepend + html.content + this.opts.html_append;
            var infowindow  = new google.maps.InfoWindow(html);
            infowindow.show = false;

            $(this.mapId).data(marker.id + 'info',infowindow);

            if (html.popup) {
                $.goMap.openWindow(infowindow, marker, html);
                infowindow.show = true;
            }

            google.maps.event.addListener(marker, 'click', function() {
                if (infowindow.show && $.goMap.opts.hideByClick) {
                    infowindow.close();
                    infowindow.show = false;
                }
                else {
                    $.goMap.openWindow(infowindow, marker, html);
                    infowindow.show = true;
                }
            });
        },

        openWindow: function(infowindow, marker, html) {
            if($.goMap.opts.oneInfoWindow)
                $.goMap.clearInfo();

            if (html.ajax) {
                infowindow.open(this.map, marker);
                $.ajax({
                    url: html.ajax,
                    success: function(html) {
                        infowindow.setContent(html);
                    }
                });
            }
            else if (html.id) {
                infowindow.setContent($(html.id).html());
                infowindow.open(this.map, marker);
            }
            else
                infowindow.open(this.map, marker);
        },

        clearInfo: function() {
            for (var i in $.goMap.markers) {
                var info = $(this.mapId).data($.goMap.markers[i] + 'info');
                if(info) {
                    info.close();
                    info.show = false;
                }
            }
        },

        getInfo: function(id, hideDiv) {
             var info = $(this.mapId).data(id + 'info').getContent();
            if(hideDiv)
                return $(info).html();
            else
                return info;
        },

        setInfo: function(id, text) {
            var info = $(this.mapId).data(id + 'info');

            if(typeof text == 'object') {
                info.setOptions(text);
            }
            else
                info.setContent(text);
        },

        getBounds: function() {
            return $.goMap.map.getBounds();
        },

        fitBounds: function(type, markers) {
            $.goMap.bounds = new google.maps.LatLngBounds();

            if(!type || (type && type == 'all')) {
                for (var i in $.goMap.markers) {
                    $.goMap.bounds.extend($(this.mapId).data($.goMap.markers[i]).position);
                }
            }
            else if (type && type == 'visible') {
                for (var i in $.goMap.markers) {
                    if($.goMap.getVisibleMarker($.goMap.markers[i]))
                        $.goMap.bounds.extend($(this.mapId).data($.goMap.markers[i]).position);
                }

            }
            else if (type && type == 'markers' && $.isArray(markers)) {
                for (var i in markers) {
                    $.goMap.bounds.extend($(this.mapId).data(markers[i]).position);
                }
            }

            $.goMap.map.fitBounds($.goMap.bounds);
        },

        addMarker: function(marker) {
            $(this.mapId).data(marker.id,marker);
            $.goMap.markers.push(marker.id);
        },

        getVisibleMarker: function(marker) {
            return $(this.mapId).data(marker).getVisible();
        },

        showHideMarker: function(marker) {
            if($.goMap.getVisibleMarker(marker)) {
                $(this.mapId).data(marker).setVisible(false);
                var info = $(this.mapId).data(marker + 'info');
                if(info.show) {
                    info.close();
                    info.show = false;
                }
            }
            else
                $(this.mapId).data(marker).setVisible(true);
        },

        getMarkerCount: function() {
            return $.goMap.markers.length;
        },

        getVisibleMarkerCount: function() {
            var vcount = 0;
            for (var i in $.goMap.markers) {
                if($.goMap.getVisibleMarker($.goMap.markers[i])) {
                    vcount++;
                }
            }
            return vcount;
        },

        setMarker: function(marker, options) {
            var tmarker = $(this.mapId).data(marker);

            delete options.id;
            delete options.visible;

            if(options.icon) {
                var toption = options.icon;
                delete options.icon;

                if(toption && toption == 'default') {
                    if (this.opts.icon && this.opts.icon.image) {
                        options.icon = this.opts.icon.image;
                        if (this.opts.icon.shadow)
                            options.shadow = this.opts.icon.shadow;
                    }
                    else if (this.opts.icon)
                        options.icon = this.opts.icon;
                }
                else if(toption && toption.image) {
                    options.icon = toption.image;
                    if (toption.shadow)
                        options.shadow = toption.shadow;
                }
                else if (toption)
                    options.icon = toption;
            }

            if (options.address) {
                $.goMap.geocode(options.address, false, {markerId:tmarker});
                delete options.address;
                delete options.latitude;
                delete options.longitude;
                delete options.position;
            }
            else if (options.latitude && options.longitude || options.position) {
                if (!options.position)
                    options.position = new google.maps.LatLng(options.latitude, options.longitude);
            }
            tmarker.setOptions(options);
        },

        getMarkers: function(type) {
            var array = [];
            switch(type) {
                case "json":
                    for (var i in $.goMap.markers) {
                        var temp = "'" + i + "': '" + $(this.mapId).data($.goMap.markers[i]).getPosition().toUrlValue() + "'";
                        array.push(temp);
                    }
                    return "{'markers':{" + array.join(",") + "}}";
                    break;
                case "data":
                    for (var i in $.goMap.markers) {
                        var temp = "marker[" + i + "]=" + $(this.mapId).data($.goMap.markers[i]).getPosition().toUrlValue();
                        array.push(temp);
                    }
                    return array.join("&");
                    break;

                default:
                    for (var i in $.goMap.markers) {
                        var temp = $(this.mapId).data($.goMap.markers[i]).getPosition().toUrlValue();
                        array.push(temp);
                    }
                    return array;
                    break;
            }

        },

        removeMarker: function(marker) {
            var index = $.inArray(marker, $.goMap.markers), current;
            if (index > -1) {
                current = $.goMap.markers.splice(index,1);
                var markerId = current[0];
                var marker   = $(this.mapId).data(markerId);
                var info     = $(this.mapId).data(markerId + 'info');

                marker.setVisible(false);
                marker.setMap(null);
                $(this.mapId).removeData(markerId);

                if(info) {
                    info.close();
                    info.show = false;
                    $(this.mapId).removeData(markerId + 'info');
                }
                return true;
            }
            return false;
        },

        clearMarkers: function() {
            for (var i in $.goMap.markers) {
                var markerId = $.goMap.markers[i];
                var marker   = $(this.mapId).data(markerId);
                var info     = $(this.mapId).data(markerId + 'info');

                marker.setVisible(false);
                marker.setMap(null);
                $(this.mapId).removeData(markerId);

                if(info) {
                    info.close();
                    info.show = false;
                    $(this.mapId).removeData(markerId + 'info');
                }
            }
            $.goMap.singleMarker = false;
            $.goMap.markers = [];
        },

        getVisibleMarkers: function() {
            var array = [];

            for (var i in $.goMap.markers) {
                if ($.goMap.isVisible($(this.mapId).data($.goMap.markers[i]).getPosition()))
                    array.push($.goMap.markers[i]);
            }
            return array;
        },

        isVisible: function(latlng) {
            return $.goMap.map.getBounds().contains(latlng);
        },

        createMarker: function(marker) {

            var options = { map:this.map };

            this.count++;

            if (marker.id)
                options.id = marker.id;
            else
                options.id = this.opts.prefixId + this.count;

            if (marker.visible == false)
                options.visible = marker.visible;

            if (marker.title)
                options.title = marker.title;

            if (marker.draggable)
                options.draggable = marker.draggable;

            if (marker.icon && marker.icon.image) {
                options.icon = marker.icon.image;
                if (marker.icon.shadow)
                    options.shadow = marker.icon.shadow;
            }
            else if (marker.icon)
                options.icon = marker.icon;

            else if (this.opts.icon && this.opts.icon.image) {
                options.icon = this.opts.icon.image;
                if (this.opts.icon.shadow)
                    options.shadow = this.opts.icon.shadow;
            }
            else if (this.opts.icon)
                options.icon = this.opts.icon;

            if (marker.address) {
                if (marker.html)
                    options.html = marker.html;

                $.goMap.geocode(marker.address, false, options);
            }
            else if (marker.latitude && marker.longitude || marker.position) {
                if (marker.position)
                    options.position = marker.position;
                else
                    options.position = new google.maps.LatLng(marker.latitude, marker.longitude);

                var cmarker = new google.maps.Marker(options);

                if (marker.html) {
                    if (!marker.html.content && !marker.html.ajax && !marker.html.id)
                        marker.html = { content:marker.html };
                    else if (!marker.html.content)
                        marker.html.content = null;

                    $.goMap.setInfoWindow(cmarker, marker.html);
                }
                $.goMap.addMarker(cmarker);
                return cmarker;
            }
        }
    }
})(jQuery);
