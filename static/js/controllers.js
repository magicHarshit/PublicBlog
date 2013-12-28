/**
 * Created with PyCharm.
 * User: harshit
 * Date: 28/12/13
 * Time: 12:14 AM
 * To change this template use File | Settings | File Templates.
 */


var blogWebsiteControllers = angular.module('blogWebsiteControllers',[]);


blogWebsiteControllers.controller('ArticleListController',['$scope','Articles',function($scope,Articles){
    $scope.articles = Articles.query();
}]);



blogWebsiteControllers.controller('ArticleDetailController',function($scope,$routeParams, $http){
   $http.get('/api/articles/' +$routeParams.articleID+'/?format=json').success(function(data){
         $scope.article= data
   });
});


blogWebsiteControllers.controller('ArticlePostController',function($scope,$routeParams, $http){

    $scope.save = function(){
        $http.post('/api/articles/',$routeParams).success(function(data){
            alert('success');
        })
    }
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