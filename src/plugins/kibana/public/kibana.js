require('plugins/kibana/discover/index');
require('plugins/kibana/visualize/index');
require('plugins/kibana/dashboard/index');
require('plugins/kibana/settings/index');
require('plugins/kibana/doc/index');
require('ui/timepicker');

const moment = require('moment-timezone');

const chrome = require('ui/chrome');
const routes = require('ui/routes');
const modules = require('ui/modules');

const kibanaLogoUrl = require('ui/images/kibana.svg');

routes.enable();

routes
.otherwise({
  redirectTo: `/${chrome.getInjected('kbnDefaultAppId', 'discover')}`
});

/*{
	id: '_plugin/head/',
	title: 'head',
	baseUrl: 'http://admin:admin@180.153.64.131:9200/'
  },
  {
	id: '_plugin/kopf/',
	title: 'kopf',
	baseUrl: 'http://admin:admin@180.153.64.131:9200/'
}*/

chrome
.setBrand({
  'logo': 'url(' + kibanaLogoUrl + ') left no-repeat',
  'smallLogo': 'url(' + kibanaLogoUrl + ') left no-repeat'
})
.setNavBackground('#222222')
.setTabDefaults({
  resetWhenActive: true,
  lastUrlStore: window.sessionStore,
  activeIndicatorColor: '#656a76'
})
.setTabs([
  {
    id: 'discover',
    title: '检索'
  },
  {
    id: 'visualize',
    title: '可视化',
    activeIndicatorColor: function () {
      return (String(this.lastUrl).indexOf('/visualize/step/') === 0) ? 'white' : '#656a76';
    }
  },
  {
    id: 'dashboard',
    title: '仪表盘'
  },
  {
    id: 'settings',
    title: '系统设置'
  },
  {
	id: 'indices',
	title: '索引管理',
	baseUrl: 'http://180.153.64.131:5602/'
  },		
  {
	id: 'test/check_mk/',
	title: '主机监控',
	baseUrl: 'http://@180.153.64.131:5001/'
  }		
])
.setRootController('kibana', function ($scope, $rootScope, courier, config) {
  function setDefaultTimezone() {
    moment.tz.setDefault(config.get('dateFormat:tz'));
  }

  // wait for the application to finish loading
  $scope.$on('application.load', function () {
    courier.start();
  });

  $scope.$on('init:config', setDefaultTimezone);
  $scope.$on('change:config.dateFormat:tz', setDefaultTimezone);
});
