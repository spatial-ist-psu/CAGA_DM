from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^start/$', 'dialogues.views.startDlg'),                   
    url(r'^stop/$', 'dialogues.views.stopDlg'),                   
    url(r'^update/$', 'dialogues.views.updateDlg'),                   
    url(r'^$', 'dialogues.views.dlgsHandler'),
)
