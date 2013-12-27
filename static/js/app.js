

var blogWebsite = angular.module('blogWebsite',['ngRoute','blogWebsiteControllers']);

blogWebsite.config(['$routeProvider',function($routeProvider){
    $routeProvider.
        when('/',{
            templateUrl:'/static/templates/article_listing.html',
            controller:'ArticleListController'
        })
}
]);