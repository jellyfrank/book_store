
/** @odoo-module **/
import {registry} from "@web/core/registry";

const serviceRegistery = registry.category("services");

const myService = {
    dependencies: ['notification'],
    start(env,{notification}){
        let counter = 1;
        setInterval(()=>{
            notification.add(`Tick Tock ${counter++}`);
        },5000);
    }
}

serviceRegistery.add('myService', myService);