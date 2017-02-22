(function(){
    'use strict';

    angular.module('MyApp', ['ngRoute'])
    .controller('MyController', MyController)
    .factory('MyFactory', MyFactory)
    .config(config);

    function MyController() {

        var vm = this;

        vm.myVal = "Halo";
        vm.message = "My message";
        vm.nickname = "Allen Stu";
        vm.linkText = "tada";
    }

    function MyFactory() {

    }

    function config($routeProvider) {
        $routeProvider
        .when('/', {
            templateUrl: 'index.html'
        });
    }

})();