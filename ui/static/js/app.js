var app = angular.module('bearTalkApp', []);

app.controller('bearTalkController', ['$scope','$http', function($scope, $http) {
    $scope.sendMessage = function() {
        param = JSON.stringify({bearId: $scope.bearId, message: $scope.currentMsg});
        $http.post('/messages', param, {headers: {'Content-Type': 'application/json'}})
             .then(function (response) {
                $scope.messages = response.data;
                $scope.currentMsg = '';
        });
    };

    $http.get('/messages').then(function (response) {
          $scope.messages = response.data;
    });
}]);