

var blogWebsiteServices = angular.module('blogWebsiteServices', ['ngResource']);

blogWebsiteServices.factory('Articles', ['$resource',
    function($resource){
        return $resource('/api/articles/?format=json', {}, {
        query: {method:'GET', isArray:true}
    });
}]);


blogWebsiteServices.factory('TagService', function ($http, $q) {
    var api_url = "/api/tags/";
    var api_suffixe = "/api/posts/";
    return {
        get: function(tag_id){
            var url = api_url + tag_id+ "/";
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function(data, status, headers, config) {
                    defer.resolve(data);
                }).
                error(function(data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        },
        list: function(){
            var defer = $q.defer();
            $http({method: 'GET', url: api_url}).
                success(function(data, status, headers, config) {
                    defer.resolve(data);
                }).
                error(function(data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        },
        query: function(text){
            var url = api_url + '?q=' + text;
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function(data, status, headers, config) {
                    defer.resolve(data);
                }).
                error(function(data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        }
    }
});
