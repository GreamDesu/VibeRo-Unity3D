using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR; //needs to be UnityEngine.VR in Versions before 2017.2
using System.IO.Ports;
using System;
using System.Net.Sockets;
using System.Net;

public class HandGrabbing : MonoBehaviour
{
    float normalizedTime = 0;
    public Animator anim;
    int data = 0;
    GameObject rotater;
    // Use this for initialization
    void Start()
    {
        anim = GetComponent<Animator>();
    }

    void Update()
    {
        data = Convert.ToInt32(TCPChat.clientMessage);
        normalizedTime = data/100f;
        anim.Play("Press", 0, normalizedTime);
        anim.speed = 0;
    }



}
