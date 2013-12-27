/**
 * Created with PyCharm.
 * User: harshit
 * Date: 28/12/13
 * Time: 12:14 AM
 * To change this template use File | Settings | File Templates.
 */


var blogWebsiteControllers = angular.module('blogWebsiteControllers',[]);

blogWebsiteControllers.controller('ArticleListController',function($scope,$http){
    $http.get('/api/articles/?format=json').success(function(data){
        $scope.articles = data
    });
});
