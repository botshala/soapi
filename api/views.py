#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.conf import settings
import requests
import json
import urllib

SO_KEY = 'XvJTrWoA7KBmRZLAsX8ERQ(('


def gen_answers(question_id):
	question_url = "https://api.stackexchange.com/2.2/questions/%s/answers?order=desc&sort=votes&site=stackoverflow&key=%s"%(question_id,SO_KEY)
	resp = requests.get(url=question_url)
	data = json.loads(resp.text)
	answer_links = [ "http://stackoverflow.com/a/%s"%i['answer_id'] for i in data['items']]
	return answer_links



def gen_image(text):
	safe_text = urllib.quote_plus(text)
	return "https://dummyimage.com/190x100/42603E/fffff.png&text=%s"%(safe_text[:30])


def index(request):
	keyword = request.GET.get("q") or 'import error'
	url = "https://api.stackexchange.com/2.2/similar?order=desc&sort=activity&site=stackoverflow&key=%s&title=%s"%(SO_KEY,keyword)
	resp = requests.get(url=url)
	data = json.loads(resp.text)

	questions_object = [ dict(id=q['question_id'],answers = gen_answers(q['question_id']),title=q['title'],image=gen_image(q['title'])) for q in data['items']]

	return JsonResponse(questions_object,safe=False)
