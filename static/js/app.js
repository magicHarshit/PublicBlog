var blogWebsite = angular.module('blogWebsite',['ngRoute','ngCookies',
                                                'blogWebsiteServices',
                                                'blogWebsiteControllers',
                                                'ui.tinymce',
                                                'firebase','ui.bootstrap']);



blogWebsite.run(function ($http, $cookies, $rootScope, $firebaseAuth) {
//    now useless no need for firebase autehntication
    var url = new Firebase('https://public-blog.firebaseio.com/');
    $rootScope.auth = $firebaseAuth(url);
//  setting global scope of user
    $http.get('/get_user/').success(function(data){
        $rootScope.user = data
        });
//    setting csrf token
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


blogWebsite.config(['$routeProvider','$httpProvider','$interpolateProvider',
    function($routeProvider,$httpProvider,$interpolateProvider){

//  it change the angular-js tag, to differentiate between django-template-tag and angular-js-tag
    $interpolateProvider.startSymbol('{{{');
    $interpolateProvider.endSymbol('}}}');

//  request.is_ajax will return True, ajax request will send the HTTP-header
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';


//    this will be used for url-routing
    $routeProvider.
        when('/articles',{
            templateUrl:'/static/templates/article_listing.html',
            controller:'ArticleListController'
        }).
        when('/articles/:articleID',{
            templateUrl:'static/templates/article_detail.html',
            controller:'ArticleDetailController'
        }).
        when('/article/post/',{
            templateUrl:'/static/templates/article_post.html',
            controller:'ArticlePostController'
        }).
        when('/users',{
            templateUrl:'/static/templates/user_listing.html',
            controller:'UserListController'
        }).
        when('/users/:userId',{
            templateUrl:'/static/templates/user_detail.html',
            controller:'UserDetailController'
        }).
        otherwise({
            redirectTo:'/articles'
        });
}
]);