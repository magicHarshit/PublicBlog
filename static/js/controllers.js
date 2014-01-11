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

   if ($scope.user.username){
        $http.get('/api/vote/?q='+$routeParams.articleID).success(function(data){
            if (data.length>0){
                $scope.userVote = data[0].vote_type
            }else{
                $scope.userVote = 0
            }
        });
   }

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
   };
   $scope.voteUp = function(article){
     $http.post('/api/update_vote/',{'article':article.id,'vote_type':1}).success(function(data){
        $scope.userVote = 1;
        $scope.$apply();
     })
   };
   $scope.voteDown = function(article){
     $http.post('/api/update_vote/',{'article':article.id,'vote_type':-1}).success(function(data){
        $scope.userVote = -1;
        $scope.$apply();

     })
   };
   $scope.markFav = function(article){
       $http.post('/api/fav_articles/',{'article':article.id}).success(function(data){
           alert('marked fav successful')
       })
   }

});


blogWebsiteControllers.controller('ArticlePostController',function($scope,$routeParams, $http,TagService){

   $scope.tags = [];
   $scope.tags_details = [];

    $scope.getTag = function (text) {
        return TagService.query(text).then(function (data) {
            return data;
        }, function (status) {
            console.log(status);
        });
    };
    $scope.selectTag = function () {
        if (typeof $scope.selectedTag === 'object') {
            $scope.tags.push($scope.selectedTag.id);
            $scope.tags_details.push($scope.selectedTag);
            $scope.selectedTag = null;
        }
    };
    $scope.removeTag = function (category) {
        var index = $scope.tags_details.indexOf(category);
        $scope.tags_details.splice(index, 1);
        var index = $scope.tags.indexOf(category.url);
        $scope.tags.splice(index, 1);
    } ;

    $scope.save = function(){
        $http.post('/api/articles/',{'title':$scope.title,'content':$scope.content,'tags':$scope.tags}).
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
   $http.post('/api/count_points/?format=json',{'user':$routeParams.userId}).success(function(data){
         $scope.points = data.points
   });
});