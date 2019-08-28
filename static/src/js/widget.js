odoo.define('require', function (require) {
    'use strict';

    var core = require("web.core");
    var Widget = require("web.AbstractAction");

    var Bing = Widget.extend({
        template: "bing",

        init: function (parent, data) {
            return this._super.apply(this, arguments);
        },

        // start: function () {
        //     return true;
        // },
        // on_attach_callback: function () { },
        // canBeRemoved: function () { }
    });

    core.action_registry.add("web.bing", Bing);

    return {
        Bing: Bing
    };

});