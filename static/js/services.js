

var blogWebsiteServices = angular.module('blogWebsiteServices', ['ngResource']);

blogWebsiteServices.factory('Articles', ['$resource',
    function($resource){
        return $resource('/api/articles/?format=json', {}, {
        query: {method:'GET', isArray:true}
    });
}]);