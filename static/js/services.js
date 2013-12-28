

var blogWebsiteServices = angular.module('blogWebsiteServices', ['ngResource']);

blogWebsiteServices.factory('Articles', '$resource',
    function($resource){
        return $resource('/api/articles/:articleId/?format=json', {}, {
        query: {method:'GET', params:{'articleId':'articleId'}, isArray:true}
    });
});