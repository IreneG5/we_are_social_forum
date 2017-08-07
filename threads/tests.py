from django.test import TestCase
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
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
    fixtures = ['subjects', 'user']

    def setUp(self):
        super(ThreadsPageTest, self).setUp()
        self.subject_id = 1

    def test_check_threads_status_code_is_correct(self):
        threads_page = self.client.get('/threads/%i/' % self.subject_id)
        self.assertEqual(threads_page.status_code, 200)

    def test_check_threads_subject_not_found(self):
        threads_page = self.client.get('/threads/999/')
        self.assertEqual(threads_page.status_code, 404)

    def test_check_threads_content_is_correct(self):
        threads_page = self.client.get('/threads/%i/' % self.subject_id)
        self.assertTemplateUsed(threads_page, "forum/threads.html")
        subject = get_object_or_404(Subject, pk=self.subject_id)
        threads_page_template_output = render_to_response("forum/threads.html", {'subject': subject}).content
        self.assertEqual(threads_page.content, threads_page_template_output)


class SubjectPageTest(TestCase):

    fixtures = ['subjects', 'user']

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)


class PostsPageTest(TestCase):
    fixtures = ['subjects', 'user', 'threads']

    def setUp(self):
        super(PostsPageTest, self).setUp()
        self.thread_id = 17

    def tearDown(self):
        del self

    def test_check_posts_status_code_is_correct(self):
        posts_page = self.client.get('/thread/%i/' % self.thread_id)
        self.assertEqual(posts_page.status_code, 200)

    def test_check_threads_subject_not_found(self):
        posts_page = self.client.get('/thread/999/')
        self.assertEqual(posts_page.status_code, 404)

    def test_check_posts_content_is_correct(self):
        posts_page = self.client.get('/thread/%i/' % self.thread_id)
        self.assertTemplateUsed(posts_page, "forum/thread.html")
        thread = get_object_or_404(Thread, pk=self.thread_id)
        posts_page_template_output = render_to_response("forum/thread.html", {'thread': thread}).content
        self.assertEqual(posts_page.content, posts_page_template_output)