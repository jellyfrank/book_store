odoo.define("book_store/static/src/js/sale.js", function (require) {
    'use strict';

    const { Component } = owl;
    const { ComponentWrapper } = require('web.OwlCompatibility');
    const FormRenderer = require("web.FormRenderer");
    const { useState } = owl.hooks;

    class PartnerOrderSummary extends Component {
        partner = useState({});

        constructor(self, partner) {
            super();
            this.partner = partner;
        }
    };

    Object.assign(PartnerOrderSummary, {
        template: "book_store.PartnerOrderSummary"
    })

    FormRenderer.include({
        async _render() {
            await this._super(...arguments);

            for (const element of this.el.querySelectorAll(".o_partner_order_summary")) {
                if(this.state.data.partner_id.res_id){
                    this._rpc({
                        model: "res.partner",
                        method: "read",
                        args: [[this.state.data.partner_id.res_id]]
                    }).then(data => {
                        (new ComponentWrapper(this, PartnerOrderSummary, useState(data[0])))
                            .mount(element)
                    });
                }
            }
        }
    });

});