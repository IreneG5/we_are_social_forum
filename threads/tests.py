from django.test import TestCase
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
from .models import Subject, Thread
from .views import threads, thread


# Create your tests here.
class SubjectPageTest(TestCase):

    fixtures = ['subjects', 'user']

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)


class ThreadsPageTest(TestCase):
    def test_check_threads_content_is_correct(self):
        threads_page = self.client.get('/threads/1/')
        # threads_page = self.client.get(reverse('threads',kwargs={'subject_id':'1'}))
        self.assertEqual(threads_page.status_code, 200)

      #  self.assertTemplateUsed(threads_page, "forum/threads.html")
      #  threads_page_template_output = render_to_response("forum/threads.html",
      #                                                    {'subject_id': 1}).content
      #  self.assertEqual(threads_page.content, threads_page_template_output)

