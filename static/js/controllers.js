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
   $http.get('/api/article/' +$routeParams.articleID+'/comments/?format=json').success(function(data){
         $scope.comments= data
   });
   $scope.addComment = function(){
       $http.post('/api/article/' +$routeParams.articleID+'/comments/',{'content':$scope.content}).
           success(function(data){
                $scope.content = '';
                $scope.comment= data
           }).
          error(function(data){
                $scope.error = data
          })
   };
   $scope.deleteComment = function(comment){
      $http.delete('/api/comment/'+comment.id+'/').success(function(data){
            alert('deleted');
      }).
      error(function(data){
              $scope.comment_deletion_error = data
          })
   }

});


blogWebsiteControllers.controller('ArticlePostController',function($scope,$routeParams, $http){

    $scope.save = function(){
        $http.post('/api/articles/',{'title':$scope.title,'content':$scope.content}).
            success(function(data){
                $scope.title = '';
                $scope.content = '';
                $scope.article = data;
                $scope.error = false
            }).
            error(function(data,status,confiq,header){
                $scope.error = data
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