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


blogWebsiteControllers.controller('ArticleDetailController',function($scope,$routeParams, $http){
   $http.get('/api/articles/' +$routeParams.articleID+'/?format=json').success(function(data){
         $scope.article= data
   });
});

blogWebsiteControllers.controller('UserListController',function($scope,$http){
    $http.get('/api/users/?format=json').success(function(data){
        $scope.users = data
    });
});

blogWebsiteControllers.controller('UserDetailController',function($scope,$routeParams, $http){
   $http.get('/api/users/' + $routeParams.userId +'/?format=json').success(function(data){
         $scope.user= data
   });
});