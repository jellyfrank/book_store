odoo.define("book_store.widget", function (require) {
    'use strict';
    
    var Widget = require("web.Widget");
    var widgetRegistry = require("web.widget_registry");

    var myWidget = Widget.extend({
        start: function(){
            console.log("my widget starting..")
        },

        destroy: function(){
            console.log("oh, my widget is dying...")
        },

        on_attach_callback: function(){
            console.log("hey, I'm attached.")
        }
    });

    widgetRegistry.add("my_widget",myWidget);
    return widgetRegistry;

});